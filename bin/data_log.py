#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import datetime
import time
import sys
import os
import urllib2
from firebase import firebase
from time import localtime, strftime, time

def main():
  LOG = "/mnt/code/log/local_data.log"
  IP  = "http://192.168.1.100"

  try:
    # Read data from sensor
    response = urllib2.urlopen(IP, timeout=2)
    html = response.read()
    temp,humid,pres,light,alarm,rasp = html.split()

    lTemp = "{0:0.1f}".format(float(temp))
    lHumid =  "{0:0.1f}".format(float(humid))
    lPres =  "{0:0.1f}".format(float(pres))

    # Read CPU temperature
    tCpu = os.popen('vcgencmd measure_temp').readline()
    lCpu = tCpu.replace("temp=","").replace("'C\n","")

    #Get date
    date = strftime("%Y-%m-%d_%H:%M", localtime())
    #Open log file to write
    f = open(LOG,'a')
    #Save data into log file
    f.write(date + ',' + lTemp + ',' + lHumid + ',' + lPres + ',' + light  + '\n')
    #Close log file
    f.close()
    #Open database connection
    dbConn = firebase.FirebaseApplication('https://raspi-weather-station-69a80.firebaseio.com', None)
    #Log data on database
    dbConn.put("/Sensors", "/Temperature/"+date, lTemp)
    dbConn.put("/Sensors", "/Humidity/"+date, lHumid)
    dbConn.put("/Sensors", "/Pressure/"+date, lPres)
    dbConn.put("/Sensors", "/CPU/"+date, lCpu)
  except Exception as err:
    print err
    print "Error reading data"

if __name__ == '__main__':
   main()


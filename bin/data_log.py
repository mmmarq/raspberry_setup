#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import datetime
import time
import sys
import sqlite3
import urllib2
from time import localtime, strftime, time

def main():
  LOG = "/mnt/code/log/local_data.log"
  DB  = "/mnt/code/log/weather_station.db"
  IP  = "http://192.168.1.100"

  try:
    # Read data from sensor
    response = urllib2.urlopen(IP)
    html = response.read()
    temp,humid,alarm,light,rasp = html.split()

    if humid is not None and temp is not None:
      lTemp = "{0:0.1f}".format(float(temp))
      lHumid =  "{0:0.1f}".format(float(humid))
      #Get date
      date = strftime("%Y,%m,%d,%H:%M", localtime())
      #Open log file to write
      f = open(LOG,'a')
      #Save data into log file
      f.write(date + ',' + lTemp + ',' + lHumid + '\n')
      #Close log file
      f.close()
      #Open database connection
      con = sqlite3.connect(DB)
      #Log data on database
      mySql = 'INSERT INTO weather_data VALUES(' + str(int(time())) + ',' + lTemp + ',' + lHumid + ')'
      with con:
        cur = con.cursor()
        cur.execute(mySql)
        con.commit()
  except:
    print "Error reading data"

if __name__ == '__main__':
   main()


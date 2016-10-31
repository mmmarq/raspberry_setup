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
  DB  = "/mnt/code/log/weather_station.db"
  IP  = "http://192.168.1.100"

  try:
    # Read data from sensor
    response = urllib2.urlopen(IP, timeout=2)
    html = response.read()
    temp,humid,pres,light,alarm,rasp = html.split()

    lTemp = "{0:0.1f}".format(float(temp))
    lPres =  "{0:0.1f}".format(float(pres))
    #Get date
    date = strftime("%Y,%m,%d,%H:%M", localtime())
    #Open database connection
    con = sqlite3.connect(DB)
    #Log data on database
    mySql = 'INSERT INTO atm_pressure VALUES(' + str(int(time())) + ',' + lTemp + ',' + lPres + ')'
    with con:
      cur = con.cursor()
      cur.execute(mySql)
      con.commit()
  except:
    print "Error reading data"

if __name__ == '__main__':
   main()


#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import datetime
import time
import sys
import sqlite3
import subprocess
from subprocess import Popen, PIPE
from time import localtime, strftime, time

def main():
  EXE = "sudo /media/2/code/raspberry_lcd/dht11"
  LOG = "/media/2/log/local_data.log"
  DB  = "/media/2/log/weather_station.db"

  while True:
    try:
      #Read sensor data twice to refresh data
      output=subprocess.check_output(EXE, shell=True)
      output=subprocess.check_output(EXE, shell=True)
      #Parse local data
      ldata = output.split()
      #Get date
      date = strftime("%Y,%m,%d,%H:%M", localtime())
      #Open log file to write
      f = open(LOG,'a')
      #Save data into log file
      f.write(date + ',' + ldata[1] + ',' + ldata[0] + '\n')
      #Close log file
      f.close()
      #Open database connection
      con = sqlite3.connect(DB)
      #Log data on database
      mySql = 'INSERT INTO weather_data VALUES(' + str(int(time())) + ',' + ldata[1] + ',' + ldata[0] + ')'
      with con:
        cur = con.cursor()
        cur.execute(mySql)
      #Stop loop
      break
    except:
      #If sensor reading fail, try again
      continue

if __name__ == '__main__':
   main()


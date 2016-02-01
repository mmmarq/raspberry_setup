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
import Adafruit_DHT
import RPi.GPIO as GPIO

def main():
  LOG = "/mnt/code/log/local_data.log"
  DB  = "/mnt/code/log/weather_station.db"

  # Set sensor type
  sensor = Adafruit_DHT.DHT22
  GPIO.setmode(GPIO.BCM)
  # Set GPIO port connected to sensor
  pin_sensor = 12
  # Read data from sensor
  humid, temp = Adafruit_DHT.read_retry(sensor, pin_sensor);
  humid, temp = Adafruit_DHT.read_retry(sensor, pin_sensor);

  if humid is not None and temp is not None:
    lTemp = "{0:0.1f}".format(temp)
    lHumid =  "{0:0.1f}".format(humid)
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

if __name__ == '__main__':
   main()


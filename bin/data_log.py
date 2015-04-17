#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import datetime
import serial
import time
import sys
import subprocess
from subprocess import Popen, PIPE
from time import localtime, strftime

def main():
  EXE = "sudo /media/2/code/raspberry_lcd/dht11"
  LOG = "/media/2/log/new_local_data.log"

  #Open log file to write
  f = open(LOG,'a')
  #Get date
  date = strftime("%Y,%m,%d,%H:%M", localtime())


  while True:
    try:
      #Read sensor data twice to refresh data
      output=subprocess.check_output(EXE, shell=True)
      output=subprocess.check_output(EXE, shell=True)
      #Parse local data
      ldata = output.split()
      #Stop loop
      break
    except:
      #If sensor reading fail, try again
      continue

  ndata = ""
  with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
    while ndata == "":
      ser.write('?')
      ndata = ser.readline().rstrip()
      time.sleep(2)
    ndata = ndata.split(',')

  #Save data into log file
  f.write(date + ',' + ldata[1] + ',' + ldata[0] + ',' + ndata[0] + ',' + ndata[1] + ',' + ndata[3] + '\n')

  #Close log file
  f.close()

if __name__ == '__main__':
   main()


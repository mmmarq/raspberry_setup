#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import datetime
import time
import sys
import smbus
from time import localtime, strftime

# for RPI version 1, use "bus = smbus.SMBus(0)" - i2c setup
i2c_bus = smbus.SMBus(1)
# This is the i2c address set in the Arduino Program
i2c_address = 0x04
#Log file name

def main():
  LOG = "/media/2/log/"+strftime("%Y-%m_local_data.log", localtime())

  i2c_bus.write_byte(i2c_address, ord('T'))
  time.sleep(0.5)
  temperature = i2c_bus.read_byte(i2c_address)

  i2c_bus.write_byte(i2c_address, ord('H'))
  time.sleep(0.5)
  humidity = i2c_bus.read_byte(i2c_address)

  #Get date
  date = strftime("%d-%m-%Y %H:%M", localtime())
  #Open log file to write
  f = open(LOG,'a')
  #Save data into log file
  f.write(date + ' ' + str(temperature) + ' ' + str(humidity) + '\n')
  #Close log file
  f.close()

if __name__ == '__main__':
   main()

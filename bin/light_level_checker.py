#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import sys
import urllib2
import time

def main():
  averageLightLevel = 0
  numReadings = 100
  readings = []
  readIndex = 0
  totalLightLevel = 0
  full = False

  IP  = "http://192.168.1.100"

  for x in range(0, numReadings):
    readings.append(0)

  while True:
    # Read data from sensor
    response = urllib2.urlopen(IP)
    html = response.read()
    temp,humid,light,alarm,rasp = html.split()

    totalLightLevel = totalLightLevel - readings[readIndex]
    readings[readIndex] = int(light)
    totalLightLevel = totalLightLevel + readings[readIndex]
    readIndex = readIndex + 1
    if (readIndex >= numReadings):
      readIndex = 0
      print "Full!"
      full = True
    average = totalLightLevel / numReadings
    print "Light level (" + str(readIndex) + "): " + str(average)
    if (average <= 85) and full: sys.exit()
    time.sleep(1)

if __name__ == '__main__':
   main()


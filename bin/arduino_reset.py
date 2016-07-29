#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libs
import RPi.GPIO as GPIO
import time

def main():
   ARDUINO_PIN = 21

   #Init GPIO pins
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(ARDUINO_PIN, GPIO.OUT)

   #Set GPIO pin HIGH for 2 seconds
   GPIO.output(ARDUINO_PIN, True)
   time.sleep(2)
   #Set GPIO pin LOW
   GPIO.output(ARDUINO_PIN, False)

if __name__ == '__main__':
   main()


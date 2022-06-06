#!/usr/bin/env python3

# working diode with delay of 6 seconds


import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)

while True:
  gpio.output(7, 1)
  time.sleep(3)
  gpio.output(7, 0)
  time.sleep(3)


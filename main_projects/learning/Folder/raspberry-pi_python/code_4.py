#!/usr/bin/env python3

import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)

while True:
  if len(input()) == 0:
    gpio.output(7, 1)
  else:
    break
  
  if len(input()) == 0:
    gpio.output(7, 0)
  else:
    break

#  str = input('enter - turn on: ')
#  if str != '':
#    break
#  else:
#    gpio.output(7, 1)
#  str = input("enter - turn off: ")
#  if str != '':
#    break
#  else:
#    gpio.output(7, 0)

gpio.cleanup()

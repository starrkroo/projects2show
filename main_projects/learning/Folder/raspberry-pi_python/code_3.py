#!/usr/bin/env python3

# working diod using button


# gpio.input  - pressed button(checks)
# gpio.output - outputs to start diod working

import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
# here is the diode
gpio.setup(7, gpio.OUT)

# here is the button
gpio.setup(3, gpio.IN)


while True:
  # false - if pressed
  # true  - if not pressed
  if gpio.input(3) == False:
    gpio.out(7, 1)
  else:
    gpio.output(7, 0)



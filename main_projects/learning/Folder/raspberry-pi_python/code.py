#!/usr/bin/env python3

import RPi.GPIO as gpio

# it sets mode to work with board
gpio.setmode(gpio.BOARD)

# calls concrete port to work
# gpio.setup(number_of_the_port, what_is_he_doing)
gpio.setup(7, gpio.out) # gpio.in

# turns on diode
# gpio.output(number_of_the_port, true=1, false=0)
gpio.output(7, 1)

# turns off
gpio.output(7, 0)

# should do with finishing of working with gpio
gpio.cleanup()

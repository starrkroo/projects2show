#!/usr/bin/env python3
import time

for k in range(1,100):
  print('Now is the {}'.format(k), end='\r')
  time.sleep(.05)

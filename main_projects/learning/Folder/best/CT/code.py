#!/usr/bin/env python3
import sys
import time

for i in range(11, 1, -1):
  sys.stderr.write(f"{i:2d}\r")
  time.sleep(.5)

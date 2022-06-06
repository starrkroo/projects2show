#!/usr/bin/env python3

def isInt(item):
  return int(item) == float(item)

isInt(122) # True
isInt(12.2) # False
isInt(12.0) # True

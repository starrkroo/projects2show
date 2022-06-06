#!/usr/bin/env python3

from huepy import *

first  = 'hello world'
second = 'somebody hello'

# NOTE: main string is first
# NOTE: minor string is second
# THEREFORE: all differents of first and second string, between them should write diff of 

def work(first, second):
  string = []
  for k1 in second.split():
    if k1 not in first:
      print(red(k1))
      if k1 in string:  continue
      string.append(k1)
  return string

print(work(first, second))
        


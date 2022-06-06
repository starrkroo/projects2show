#!/usr/bin/env python3

file = input("Filename: ")
with open(file) as f:
  first = f.read()

from huepy import *

file2 = input("Filename: ")
with open(file2) as f:
  second = f.read()

def work(first, second):  
  # define which one string is biggest
  output_string = ''

  for k in second.split():
    if k not in first:
      output_string += red(k) + ' '
      continue
    
    output_string += green(k) + ' '
 
  return output_string
    

if len(first) > len(second):
  print(work(second, first))
else:
  print(work(first, second))

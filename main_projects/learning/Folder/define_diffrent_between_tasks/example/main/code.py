#!/usr/bin/env python3


from config import NEVER_READ
from huepy import *
from os import listdir
from os.path import isfile

path = '.ddifer/'

def work(first, second):
  # NOTE: second must be biggest

  output_string = ''

  for k in second.split():
    if k not in first:
      output_string += red(k) + ' '
      continue
    
    output_string += green(k) + ' '

  return output_string

# runs in current directory
for k in listdir('.'):
  if k in NEVER_READ: continue
  if isfile(k):
    with open(k) as f1:
      with open(path + k) as f2:
        first  = f1.read()
        second = f2.read()
        if len(first) > len(second):
          print(work(second, first))
        else:
          print(work(first, second))

        

#!/usr/bin/env python3
from time import sleep

item = '|'
items = [k for k in r'\|/-']

def work1(string, object): # slash
  for k in range(1, object):
    for i in items:
      if '|' in string:
        sleep(0.5)
        print(string.replace('|', i), end='\r')
      else:
        print("Haven't {}".format(items))
        exit()

#!/usr/bin/env python3

# python -i some.py

from os import getpid, system, popen
from sys import argv

def call(name):
  while True:
    got_info = (popen("ps aux | grep {}".format(name)).readlines())
    for index, k in enumerate(got_info):
      if "R+" in k:
        print("Is executing")
        break
      else:
        print('NOPE')

if __name__ == "__main__":
  argv.pop(0)
  if not argv: # or len(argv) < 2:
    exit()
  else:
    #print(argv[0], argv[1])
    print(argv[0])
    call(argv[0])
    

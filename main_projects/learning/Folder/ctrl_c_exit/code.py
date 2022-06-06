#!/usr/bin/env python3

from huepy import *

def event_loop():
  print(red("Enter text: "), end='')
  x = str(input())
  print("You inputed {}".format(x))


if __name__ == "__main__":
  try:
    event_loop()
  
  except KeyboardInterrupt:
    print("\nexited")

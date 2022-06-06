#!/usr/bin/env python3
from sys import argv

def loop(item):
  print(item[::-1])

if __name__ == "__main__":
  argv.pop(0)
  if not argv:
    print("Arguments is empty. Should write a string")
    exit()
  else:
    for param in argv:
      loop(param)

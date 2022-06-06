#!/usr/bin/env python3

import os, fnmatch
from sys import argv
from os import getlogin
def find(pattern, path):
  result = []
  for root, dirs, files in os.walk(path):
    for name in files:
      if fnmatch.fnmatch(name, pattern):
        result.append(os.path.join(root, name))
  return result

if __name__ == '__main__':
  argv.pop(0)
  if not argv:
    exit()
  else:
    for k in (find(argv[0], '/home/{}'.format(getlogin()))):
      print(k)

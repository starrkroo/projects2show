#!/usr/bin/env python3

# saves all config in mine dir
from os import listdir
from os import mkdir
from os.path import isfile
from huepy import *
from config import NEVER_READ

name_path = '.ddifer'
try:
  mkdir(name_path)
except:
  pass
  

for k in listdir():
  if k in NEVER_READ: continue
  if isfile(k):
    try:
      with open(k) as f1:
        with open('{}/{}'.format(name_path, k), 'w') as f2:
          f2.write(f1.read())
    except:
      print(red("Delete file <{}>".format(k)))



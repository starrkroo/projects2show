#!/usr/bin/env python3

from urllib.requests import urlopen
from huepy import *

def connected(url = 'https://google.com'):  
  try:
    urlopen(url)
    return True
  else:
      return False

if connected('vk.com'):
  print(green("Your Network is fine!"))
else:
  print(red("Check your Network connection"))

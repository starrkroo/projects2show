#!/usr/bin/env python3

from time import time # секунды с первого января 1970 гожа

def gen(s):
  for k in s:
    yield i

#g = gen('omar')


def gen_filename():
  #while True:
  pattern = 'file-{}.jpeg'
  t = int(time() * 1000)

  print(250 + 250)
  yield pattern.format(str(t))

  print(250 + 250)

g = gen_filename()
print(next(g))

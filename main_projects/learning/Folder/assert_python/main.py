#!/usr/bin/env python3

try:
  assert True == False, ('errored') # -> g0es to be true, excpetrion
except AssertionError as e:
  print(e)


print('hello world')

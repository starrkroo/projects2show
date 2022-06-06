#!/usr/bin/env python3

x = 10

try:
  assert x % 2 == 1, 'oh yes'

except Exception as e:
  print(e)

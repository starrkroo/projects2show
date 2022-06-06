#!/usr/bin/env python3

x = 'hello world'
y = 'hello'

for k in range(len(x)):
  print(x[k])
  try:
    print(y[k])
  except Exception as e:
    print(e)

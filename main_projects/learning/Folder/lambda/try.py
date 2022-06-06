#!/usr/bin/env python3

x = int(input(": "))
y = int(input(": "))

item = lambda x, y: x*y
print(item(x, y))

# NOTE: writes in var to args which is multiplicating

def work(x, y):
  return x*y
item = work(x,y)
print(item)

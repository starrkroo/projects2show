#!/usr/bin/env python3

item = 10

def foo():
  global item

  global shit
  shit = 1000
  
  item = 20
  print(item)

print(item) # prints first exist item
foo()       # makes global item which owned previous global var item
print(item) # prints new item

def _try():
  print(shit)
_try()

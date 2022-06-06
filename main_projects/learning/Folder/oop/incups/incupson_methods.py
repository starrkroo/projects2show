#!/usr/bin/env python3

class A:
  def __private(self):
    print('some bullshit')


x = A()
try:
  x.__private()
except Exception as e:
  print(e)  
  print()
  x._A__private()

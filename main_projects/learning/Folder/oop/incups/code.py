#!/usr/bin/env python3

class work:
  def __init__(self, first, second):
    self.first = first
    self.__second = second

  @property
  def output(self): 
    return "{} - {}".format(self.first, self.__second)

x = work(1, 2)
print(x.output)
print(x.first)

try:
  print(x.second)
except Exception as e:
  print(e)

print(x._work__second)

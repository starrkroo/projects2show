#!/usr/bin/env python3

class Person:
  def __init__(self, time, name):
    self.__time = time
    self.name   = name

  def output(self):
    print("Your name is {}".format(self.name.upper()))

obj = Person(2, 'starrk')
obj.output()

print(obj._Person__time)

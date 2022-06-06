#!/usr/bin/env python3

class Working:
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def __add__(self, other):
    return self.first + self.first

tems = Working(2, 4)
tem2 = Working(5, 10)
print(tems + tem2)

#!/usr/bin/env python3

# TODO

class Work:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    return (self.x + other.x)

object1 = Work(3, 4)
object2 = Work(6, 8)

result = object1 + object2 # --> 3 + 6

print(result)

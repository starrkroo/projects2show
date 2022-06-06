#!/usr/bin/env python3




"""
__add__ = '+'


"""

class Work:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    # self.x  = 5;
    # other.x = 3;
    ############## 
    # self.y  = 7
    # other.y = 9


    print(self.x)
    return Work(self.x + other.x, self.y + other.y)

first = Work(5, 7)
second= Work(3, 9)

result = first + second

print(result.x)
print(result.y)

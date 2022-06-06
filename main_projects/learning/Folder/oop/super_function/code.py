#!/usr/bin/env python3

class A:  
  def __init__(self, first, second):
    self.first = first
    self.second = second
  #@property
  def output(self):
    return "{} - {}".format(self.first, self.second)

class B(A):
  def __init__(self, first, second, third):
    # self.first = first
    # self.second = second
    super().__init__(first, second)

    self.third = third
  def output(self):
    return "{} - {} - {}".format(self.first, self.second, self.third)

object1 = B(1,2,3)
print(object1.output())

object2 = A(1, 2)
print(object2.output())

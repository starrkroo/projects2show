#!/usr/bin/env python3

class Human:
  def __init__(self, age):
    self.age = age
  
  @property
  def get_age(self): 
    return "Age is {}".format(self.age)

object = Human(16)
print(object.get_age)


"""
So, it means that you can't use j constructions in code, because it is not reading all
"""

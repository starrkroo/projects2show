#!/usr/bin/env python3

class Person:
  def __init__(self, name, age, height, weight):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight

  @property
  def all(self):
    return "{} has: \nage {},\nheight {},\nweight {}".format(name, age, height, weight)


class Human(Person):  
  def __init__(self, dick_size, name, age, height, weight):
    self.ds = dick_size
    super().__init__(self, name, age, height, weight)

  def all(self):
    return "{} has: \nage {},\nheight {},\nweight {}\n dick size {}".format(name, age, height, weight, dick_size)


object = Person('bald from brazzers', 30, 180, 70)
object.all

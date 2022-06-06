#!/usr/bin/env python3
class work:
  def __init__(self, first, second):
    self.first = first
    self.__second = second

  @property
  def output(self): 
    return "{} - {}".format(self.first, self.__second)

class work2(work):
  def __init__(self, first, second, third):
    super().__init__(first, second)
    self.third = third

  @property
  def output(self):
    try:
      return '{} - {} - {}'.format(self.first, self.__second, self.third)
    except Exception as e:
      print(e)
      return '{} - {} - {}'.format(self.first, None, self.third)

  
x = work2(3, 4, 5)
print(x.output)

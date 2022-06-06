#!/usr/bin/env python3

#TODO: should steal all attributes of parent class 


class Move():
  def __init__(self, hello, world):
    self.h = hello
    self.w = world

  def start(self):
    print(self.h, end=' ')
    print(self.w)

class Ahah(Move):
  def __init__(self, kek,  hello, world):
    super().__init__(hello, world)
    self.kek = kek

  def heloo(self):
    print(self.kek)
  def output(self):
    print(self.h)

superman = Move('hello', 'wordl')
superman.start()


super_man = Ahah('hello', 'worldld', 'lel')
super_man.heloo()
#super_man.start()
super_man.output()

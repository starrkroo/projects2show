#!/usr/bin/env python3

class Phone:
  def __init__(self, price, display, camera):
    self.price = price
    self.display = display
    self.camera = camera
  
  @property
  def make_photo(self):
    print("I did photo!")

class Iphone(Phone):
  def __init__(self, price, display, camera, apple = True):
    super().__init__(price, display, camera)
    self.apple = apple
    
  @property
  def make_photo(self):
    print("I did photo on iphone!")

xiaomi = Phone(5000, 720, 2.5)
xiaomi.make_photo

iphone_x = Iphone(50000, 1920, 10.5)
iphone_x.make_photo

#!/usr/bin/env python3

from datetime import datetime
def timeit(func):
  def wrapper():
    current_time = datetime.now()
    func()
    print("First is {}".format(datetime.now() - current_time))
    return func
  return wrapper

@timeit
def first():
  from os import system
  system("echo hello_world1")

@timeit
def second():
  import os
  os.system("echo hello_world2")

first()
second()

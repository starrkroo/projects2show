#!/usr/bin/env python3
from threading import Thread
from time import sleep

def work(n, item):
  print("I am {}".format(item))
  sleep(n)
  print("after sleep")

t = Thread(target=work, name='Thread1', args=(2, 'fucking you'))

t.start()

t.join()

#!/usr/bin/env python3


def work():
  yield 1
  yield 2
  yield 3

g = work()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

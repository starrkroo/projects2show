#!/usr/bin/env python3


def linear(k, b):
  return lambda x: x*k+b

graf1 = linear(2,5)
print(graf1(3))

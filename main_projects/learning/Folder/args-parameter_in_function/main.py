#!/usr/bin/env python3

def summa(*args):
  return sum(args)


print(summa(1, 2, 3, 4))

def summa(*args):
  for i in args:
    print(i)

summa(1, 2, 3, 4)

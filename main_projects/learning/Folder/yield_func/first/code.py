#!/usr/bin/env python3

def gen(s):
  for i in s: 
    yield i

g = gen('omar')
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))



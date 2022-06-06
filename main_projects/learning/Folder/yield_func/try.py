#!/usr/bin/env python3


def generate(*args):
  for k in args:
    yield k


print(next(generate('hello', 'world')))

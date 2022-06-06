#!/usr/bin/env python3

def foo():
  return 'bar'

with foo as f:
  f()

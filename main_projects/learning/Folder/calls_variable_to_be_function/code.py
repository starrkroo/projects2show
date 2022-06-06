#!/usr/bin/env python3

def foo(intg, power):
  return intg**power

shit = foo # calls shit to be a new name of function
print(shit(2, 3))

shit = foo(2, 4) # saves in shit returned values from function foo
print(shit)

shit = 10
print(shit)

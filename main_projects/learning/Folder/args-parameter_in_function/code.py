#!/usr/bin/env python3

#
## args   - tuple
## kwargs - dictionary
#
def some(*args, **kwargs):
  print(sum(args))
  print(kwargs)

x  = [1, 2, 3]
some(*x, item='hello world', what='what?')


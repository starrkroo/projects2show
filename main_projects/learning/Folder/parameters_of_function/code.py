#!/usr/bin/env python3

# NOTE: IDK how to get error here 
## TODO: I think should use:
#                    def work(item=10)

tru = 10

def foo(item = tru, shit = tru):
  return item, shit

print(foo(shit = 20))

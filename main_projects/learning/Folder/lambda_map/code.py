#!/usr/bin/env python3

# map(function, item)
############# 
# def work(item):
#   print(item)
# list(map(work, [1, 2, 3])

def work(x):
  print(x)

x = map(work, [1, 2, 3])
(list(x))

print()
################################################################################################
print()

array = [1, 2, 3]

x = list(map(lambda x: print(x), array))

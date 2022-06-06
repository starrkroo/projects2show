#!/usr/bin/env python3

# object.rand(x,y) - random values with table x in row and y in column
# object.ones() - adding value 1 to the score
# object.size() - returning table
# object.add(x) - addition table to x (object unchanged)
# object.add_(x) - addition table to x (object changed)

import numpy as np
import torch
import helper

#create 
#     4 in row
#     5 in column
#+--+--+--+--
# [] [] [] []
# [] [] [] []
# [] [] [] []
# [] [] [] []
# [] [] [] []
#+--+--+--+--
#x = torch.rand(5,4)

x = torch.rand(2,1)

print(x)
print()


# this one is changing created table to ones
# y = torch.ones(5, 2) - that is too table which is getting values
y = torch.ones(x.size())
print(y)


print()
# printing sum of x and y
#       x - some random values
#       y - values of ones
z = x + y
#print(z.add(2))

print()
# it is simmilar to be a massive
print(z[0])

print()
print(z[:, 1:])

print()
print(z.add(1))

#print(z)
#print(z.add_(1)
#print(z)

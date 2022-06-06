#!/usr/bin/env python3

import torch

x = torch.rand(2,1)
print(x)
print()

#y = torch.ones(5, 2)
y = torch.ones(x.size())
print(y)
print()

z = x + y
print(z)

print()
print(z.add_(1))

print('\n \n \n')
print(z.size())


# reshaping that to be around of the first table
print(z.resize_(1,2))

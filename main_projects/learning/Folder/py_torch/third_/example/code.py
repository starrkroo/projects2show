#!/usr/bin/env python3

import torch

x= torch.zeros(1, requires_grad=True)
print(x, '\n')

with torch.no_grad():
  y = x+2

print(y, '\n')
print(y.requires_grad)

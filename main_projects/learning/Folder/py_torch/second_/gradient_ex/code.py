#!/usr/bin/env python3


import torch

x = torch.zeros(1, requires_grad=True)
with torch.no_grad():
  y = x*2
  print(x)
  print()
  print(y)
print(x.requires_grad)
print(y.requires_grad)

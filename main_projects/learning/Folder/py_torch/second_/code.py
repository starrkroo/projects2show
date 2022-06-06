#!/usr/bin/env python3

#TODO: use in function to get values from grad:::::::
#                   object.requires_grad
#                   object.mean()
#                   object.grad_fn
#                   object.grad

from collections import OrderedDict
import numpy as np
import time
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

x = torch.randn(2,2, requires_grad=True)
print(x); print(x.requires_grad); print()

y = x**2
print(y); print(y.requires_grad); print()
print('\n\n\n\n\n')



#print(y.grad_fn)
#print(y.mean())
z = y.mean()
print(z)

print(x.grad)

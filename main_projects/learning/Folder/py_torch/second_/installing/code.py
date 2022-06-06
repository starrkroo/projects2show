#!/usr/bin/env python3

import torch
import numpy as np

a = np.random.rand(4,3)
print(a, '\n')

#print(a, '\n')

b = torch.from_numpy(a)
#print(b)
#print(b.numpy(), '\n')

# variable [a] is object of numpy
# variable [b] is object of torch

print(b.mul_(2))
print(a)
#print(a)
#print(a)


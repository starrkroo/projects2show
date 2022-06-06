#!/usr/bin/env python3

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

x = torch.randn(2,2, requires_grad=True)
print(x)
print(x.grad_fn)

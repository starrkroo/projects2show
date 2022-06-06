#!/usr/bin/env python3

import numpy as np

a = np.arange(2,5)
print(a)
print()
#print(a.shape)

a.resize(2,5)
print(a.shape)

print(type(a))
print(type(a.resize()))

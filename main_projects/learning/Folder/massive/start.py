#!/usr/bin/env python3


x = [k for k in range(int(input(': ')))]


print(x[2:10:2])
y = x[:]

y[2] = 200

print(y[2:10:2])

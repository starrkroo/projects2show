#!/usr/bin/env python3

a, b = 2, 3
item = lambda x,y : x**y
print(item(a, b))

a, b = 2, 3
item = lambda x=a,y=b : x**y
print(item())

#!/usr/bin/env python3
x  = 'try.py'
_x = ''

item = x.split('.')

attr = list(item[0])

attr.append('_1.')
attr.append(item[1])
print(item[1])

#item = list(map(

for k in attr:
  _x += k

print(_x)

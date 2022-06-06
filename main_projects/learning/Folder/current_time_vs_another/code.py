#!/usr/bin/env python3

from time import ctime

first = ctime().split()[3]
another = '16:56:40'

if first.split(':')[0] >= another.split(':')[0] and first.split(':')[1] >= another.split(':')[1] and first.split(':')[2] >= another.split(':')[2]:
  print('hello worl')


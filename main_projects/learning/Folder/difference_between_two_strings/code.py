#!/usr/bin/env python3

first  = input(': ')
second = input(': ')

def difff(first, second):
  return [i for i in range(len(first)) if first[i] != second[i]]

print(difff(first, second))

#!/usr/bin/env python3

def upper(string):
  return string.upper()

l = ['one', 'two', 'three']

# first - function
# second - 

#TODO: 
# first argument is what to do with your object
# second argument with what to do this one

new_list = list(map(upper, l))


new_list_2 = map(lambda string: string.upper(), l)



print(new_list)

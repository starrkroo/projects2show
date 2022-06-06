#!/usr/bin/env python3

class work:
	def __init__(self, first, second):
		self.first = first
		self.second = second
	
	def __add__(self, other):
		return (self.first + other.second)

o1 = work(4, 6)
o2 = work(6, 8)

print(o1 + o2)

	

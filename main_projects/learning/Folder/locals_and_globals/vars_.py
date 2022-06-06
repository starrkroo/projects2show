#!/usr/bin/env python3


class Test(object):
	a = 'one'
	b = 'two'
	def frobber(self):
		print (self.c)
t = Test()
huh = vars(t)
huh['c'] = 'three'
t.frobber()


def test():
	a = 1
	b = 2
	print (test.c)
huh = vars(test)       # these two lines are the same as 'test.c = 3'
huh['c'] = 3
test()


#!/usr/bin/env python3


#print(locals())
#print()
#print(globals())
#print()
#print(vars())
##print()


def test():
	a = 1
	b = 2
	huh = locals()
	c = 3
	print(huh)
	huh['d'] = 4
	print(locals())
	print(d)

test()

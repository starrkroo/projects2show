#!/usr/bin/env python3

mass = [k for k in range(10)]

#insert(place, num)
#insert( len(mass), 9) - insert value in the last object in there

mass.insert(1,5)
print(mass)

mass.remove(1) # deleting massive
print(mass)

print(mass.pop()) # deleting last item in the massive
print(mass)

#mass.clear() # deleting all in the massive
#print(mass)

print(mass.index(4)) # returns index of the massive 
# >>> 4

print(mass.count(5)) # returns count of coming in the massive
# >>> 2

mass.sort() # sorting values in the massive
print(mass)

mass.reverse() # reversing values in the massive ( perevorachivaet )
print(mass)



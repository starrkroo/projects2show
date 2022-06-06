#!/usr/bin/env python3

def gen1(s):
  for i in s:
    yield i

def gen2(n):
  for i in range(n):
    yield i

#def gen3(sur):
#  for i in sur:
#    yield i


g1 = gen1('omasta')
g2 = gen2(6)
#g3 = gen3('mahmudov')

tasks = [g1, g2]#, g3]
print(tasks.append(tasks.pop(0)))

while tasks:
  task = tasks.pop(0)

  try:
    i = next(task)
    #print(i)
    tasks.append(task)
  
  except StopIteration:
    pass


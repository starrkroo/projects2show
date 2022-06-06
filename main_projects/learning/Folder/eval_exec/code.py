#!/usr/bin/env python3

a = 2
eval('37 + a')

try:
  eval('x = 2')
except:
  print("Видимо нет((")

exec('x = 2')
print(x)

try:
  exec('37 + a')
except:
  print("Видимо да. но все равно вывод - None")

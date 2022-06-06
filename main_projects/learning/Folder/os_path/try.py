#!/usr/bin/env python3

from os.path import *
from os import *

print(abspath('.'))

print(dirname(abspath('../')))

print(exists('try.py'))

print(getctime('code.py'))

print(getsize('code.py'))

print(isfile('code.py'))

print(isdir('code.py'))

print(mkdir(path.join(path.abspath('.'), 'code123123123123123123.py')))

print(path.split(path.abspath('.' + 'shit.py')))

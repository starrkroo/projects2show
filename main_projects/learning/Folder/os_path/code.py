#!/usr/bin/env python3

from os import path
import os

print(path.abspath('.'))                                # current directory

print(path.basename('/home/starrk/coding/learning'))    # base directiory [idk]

print(path.dirname(path.abspath('.')))                  # parent directory (previous dir)

print(path.exists('code.py'))                           # returns True if file exists and False if file is not exists

print(path.getctime('code.py'))                         # last work with file [getctime, getmtime, getatime]

print(path.getsize('code.py'))                          # returns size of the file in bytes

print(path.isabs(path.abspath('.')))                    # returns true if abs path

print(path.isfile('code.py'))                           # is file - file or no

print(path.isdir('.'))                                  # is dir or no

print(path.join(path.abspath('.'), 'code123123123123123123.py'))          # connect to the some file in there

print(path.split(path.abspath('.' + 'code.py')))        # returns list with the path and file



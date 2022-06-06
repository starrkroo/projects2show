#!/usr/bin/env python3
from os import getcwd

with open('{}/../opening_file_with_dir/another.py'.format(getcwd()), 'w' ) as f:
  f.write("item = 'hello world'")

#!/usr/bin/env python3

from fuzzywuzzy import fuzz
print(fuzz.ratio('hello world', 'hello jim'))
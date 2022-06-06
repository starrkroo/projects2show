#!/usr/bin/env python3
from tqdm import tqdm
from time import sleep

array = [k for k in range(10)]

for k in tqdm(range(100), desc = 'bullshit'):
  sleep(.5)
  pass

#!/usr/bin/env python3

def item(x):
  if x>0:
    return 'positive'
  else:
    return 'negative'

item = lambda x: 'positive' if x>0 else 'negative'

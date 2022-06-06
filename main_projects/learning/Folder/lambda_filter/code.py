#!/usr/bin/env python3

# filtering
# filter(function(condition, item))

x = list(filter(lambda x : x%2 == 0, [k for k in range(1, 100)]))
print(x)



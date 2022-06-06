#!/usr/bin/env python3

import os
f = os.popen('ls')
rd = f.read()
print( rd )
f.close()

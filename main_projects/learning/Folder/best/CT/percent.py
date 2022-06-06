#!/usr/bin/env python3

import sys
import time
for i in range(100):
	sys.stdout.write("\rInstallation Progress: %d percent" % i)
	time.sleep(.05)

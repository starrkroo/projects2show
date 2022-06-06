#!/usr/bin/env python3

from sys import *
import socket

# sys.argv - values which given in python programm at start
print(argv)

# sys.executable - absolute path to the python compiler
print(executable)

# sys.path - path of imported files
print(path)
path.append("/path/to/my/module")
print(path)

# sys.platform - current operation system
print(platform)


# sys.exit() - exit (callable)
exit("Programm fucked you")




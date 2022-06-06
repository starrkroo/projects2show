#!/usr/bin/env python3

import ctypes, sys

def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False

if is_admin():
  print('suck my dick')
else:
  # Re-run the program with admin rights
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

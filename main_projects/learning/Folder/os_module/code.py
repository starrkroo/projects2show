#!/usr/bin/env python3

from os import *

# os.name - information about system with what you are working 
print(name)

# os.environ - information of enviroment
#print(environ) # - outputs all of enviroment objects
print(environ['LOGNAME'])

# same code, but arguments need to be a key
print(getenv('LOGNAME'))

# os.getcwd() - absolute path to the compiled programm
print(getcwd())
item = getcwd()

# os.chdir(path) - changes current directory to 'path'
chdir(getcwd() + "/../../")
print(popen('ls -l').read());         chdir(item)

# os.mkdir(directory_name) - makes directory
#mkdir('hello_world')

#os.makedirs(path) - mkdir -p hello_world2/shit_fuck
#makedirs(getcwd() + "/hello_world2/2019/25;05/FUCKYOU")

# os.remove(file) - removes files
system('touch siht.txt')
print(listdir())
remove('siht.txt')
print(listdir())

# os.rmdir(dir) - removes directory
mkdir('hello_world')
listdir()
rmdir('hello_world')
listdir()

# os.rename(file, new_name) - renames file
try:
  rename('item.txt', 'shit.txt')
except:
  rename('shit.txt', 'item.txt')

# os.walk - 

for root, dirs, files in walk(getcwd()):
  print(files) # files in this directory
  print(dirs)  # some kind of shit
  print(root)  # abs path to the file




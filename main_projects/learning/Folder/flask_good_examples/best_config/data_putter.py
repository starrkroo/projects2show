#!/usr/bin/env python3

import sqlite3
from huepy import *

conn = sqlite3.connect('information.db')
cursor = conn.cursor()

def show_all():
  try:
    cursor.execute("SELECT * FROM Work")
  except Exception as e:
    print(red(e))
    exit()
  print("All data{} \n\t{} ".format(orange(":"), green(cursor.fetchall())))
  
  user_choice = input(" Delete data?(\nyes/y - delete\nno/n - do not delete: \n")
  if user_choice == 'yes' or user_choice == 'y':
    cursor.execute("DROP TABLE Work")
  elif user_choice == "no" or user_choice == "n":
    pass


#def putThis(login, password):
#  try: cursor.execute("DROP TABLE Work") 
#  except: pass
#  cursor.execute('CREATE TABLE IF NOT EXISTS Work(login VARCHAR(10), password VARCHAR(10))')
#  query = """INSERT INTO Work (login, password) VALUES(?, ?)"""
#  cursor.execute(query, (login, password))
#########################################################################################33
  #cursor.execute("""CREATE TABLE IF NOT EXISTS Work (
  #  'id INTEGER PRIMARY KEY AUTOINCREMENT,
  #  login VARCHAR(10), 
  #  password VARCHAR(10)
  #  ')
 # 
 # """)

 # conn.commit()


if __name__ == "__main__":
  #putThis('hello', 'world')
  show_all()

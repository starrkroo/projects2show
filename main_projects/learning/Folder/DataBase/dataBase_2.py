import sqlite3
def dataBase(login,password):
  conn = sqlite3.connect("test_2.db")
  cursor = conn.cursor()
  cursor.execute('DROP TABLE Try_2')
  cursor.execute('''CREATE TABLE IF NOT EXISTS Try_2(
    login VARCHAR(20),
    password VARCHAR(20)
    )''')
  query = ("INSERT INTO Try_2 (login,password) VALUES(?,?)")
  cursor.execute(query, (login,password))
  cursor.execute('SELECT * FROM Try_2')
  print(cursor.fetchall())
  conn.commit()
  cursor.close()
  conn.close()
# dataBase()
x = input("Enter your login: ")
y = input("Enter your password: ")
dataBase(x,y)

def setForm():
  conn = sqlite3.connect('test_123.db')
  cursor = conn.cursor()
  cursor.execute("DROP TABLE users")
  cursor.execute("""CREATE TABLE IF NOT EXISTS users
  (
  -- id INTEGER PRIMARY KEY AUTOINCREMENT,
  login VARCHAR(30),
  password VARCHAR(30)
  )
  """)
  query = """INSERT INTO users (login, password)
  VALUES (?, ?)"""
  cursor.execute(query, ('omar', 'omar_2'))
  cursor.execute("SELECT * FROM users") 
  print(cursor.fetchall())
	
  conn.commit() # fixation of dates 
	
  cursor.close()
  conn.close()
# setForm()

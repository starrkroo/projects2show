#!/usr/bin/env python3


from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def putThis(login, password):
  conn = sqlite3.connect('information.db')
  cursor = conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Work(login VARCHAR(10), password VARCHAR(10))')
  query = """INSERT INTO Work (login, password) VALUES(?, ?)"""
  cursor.executemany(query, [(login, password)])
  conn.commit()
  cursor.close()
  conn.close()

@app.route('/')
def bullshit():
  return redirect('/register')  

@app.route('/register')
def index():
  return render_template('index.html')

@app.route('/register', methods=['POST'])
def index_form():
  item = request.form['login']
  password = request.form['password']

  putThis(item, password)

  putThis(item, password)
  return render_template("successed.html")



@app.route('/auth')
def auth():
  return render_template('auth.html')

@app.route('/auth', methods=['POST'])
def auth_checkForm():
  conn = sqlite3.connect('information.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Work")
  item = request.form['login']
  password = request.form['password']
  print(item)
  
  for k in cursor.fetchall():
    if item in k[0] and password in k[1]:
      name = item
      return render_template('wellcome.html', username = name)
  return 'shit. try again'

  cursor.close()
  conn.close()


if __name__ == "__main__":
  app.run(port=5001, debug = True)

#!/usr/bin/env python3
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from huepy import *

app = Flask(__name__)
app.config['UPLOAD_PATH'] = '/home/starrk/Learning/python-learning/cloud/frame/files'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def index_form():
  file = request.files['file']
  f = file
  f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))

  print('good')
  return render_template('heh.html')


if __name__ == '__main__':
  app.run(debug=True)



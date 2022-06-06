#!/usr/bin/env python3

class Post:
  def __init__(self, title, body):
    self.title = title
    self.body = body

a = Post(title = 'a', body = 'a')
print(a)

print('\n'*3)

class Post:
  def __init__(self, title, body):
    self.title = title
    self.body = body

  def __repr__(self):
    return '<Post title: {}, body: {}'.format(self.title, self.body)

a = Post(title = 'a', body = 'a')
print(a)

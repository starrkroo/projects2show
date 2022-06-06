#!/usr/bin/env python3

from code import Creation

server = []

alph = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

class Start():
  def __init__(self, alph):
    self.al = alph
    self.start()

  def start(self):

    for k in range(26):

      exec('var_' + str(k) + ' = ' + str("self.al[k]"))
      server.append(locals()['var_' + str(k)])

# At this part we get variables from var_1 to var_26

    #print(locals()['var_' + str('2')])

    #print("Server massive is: \n", server)


text = input("Enter a text: ")
object    = Start(alph)
object_2  = Creation(text)

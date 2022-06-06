#!/usr/bin/env python3

class Putin:
  def __init__(self, time, promises):
    self.__time = time
    self.promises = promises

#def make_promises(self):
#	print('Обещаю' + self.promises)
  
  def getter(self, value): # описываем метод доступа к свойству 
    print('Шиш тебе!')
  
  def setter(self):#, value): # описываем метод, который меняет значение свойства
    print('Сколько хочу - столько и правлю!')

  time = property(setter, getter) # связка свойства и геттера с сеттером

clon_1 = Putin('(><)', input('Предвыборные обещания: '))

print(clon_1._Putin__time)
clon_1.time = 0

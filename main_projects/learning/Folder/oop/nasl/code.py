#!/usr/bin/env python3

#class Hello:
#  def __init__(self, v):
#    # v = self.value -- pishem shto attribute 'v' budet v rabote == self.value
#    self.value = v



class Hero:
  def __init__(self, strength, side):
    self._strength = strength
    self.side = side

  def punch(self):
    return self.strength

  def save(self):
    print('Боже, храни Америку!')

class X_men(Hero): # унаследовал базовый класс Hero
  def _fly(self):
    print('Палундра!!')

class New_X_men(X_men):
  def __init__(self, strength, side, teacher):
    self.strength = strength
    self.side = side
    #super().__init__(self, strength, side)
    self.teacher = teacher

  def fly(self):
    print('Свистать всех наверх!')

superman = Hero(500, 'лигасправедливости')
logan = X_men(100, 'люди х')
fenix = New_X_men(1000, True, 'hello')

print(logan.side)
logan.save()
logan._fly()
### superman.fly() # нельзя вызывать метод дочернего класса для объекта базового класса
print(fenix.strength)
fenix.fly()
print(fenix.teacher)


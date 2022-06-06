
class employee:
  def __new__(cls, item):
    cls = 'someshit'
    print(item)
    print ("__new__ magic method is called")
    #inst = object.__new__(cls)
    #return inst
  def __init__(self, item):
    print ("__init__ magic method is called")
    #self.name='Satya'


e1 = employee('hello')

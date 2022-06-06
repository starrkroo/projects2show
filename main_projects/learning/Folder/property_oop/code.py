class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    # makes function like a variable of class 
    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

person = Person("Omar", "Starrk")
print(person.first_name)
print(person.last_name)

print(person.full_name)

print('\n'*5)
##################################################################################################################################
""" 
        same code:
"""

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    # makes function like a variable of class 
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

person = Person("Omar", "Starrk")
print(person.first_name)
print(person.last_name)

print(person.full_name())
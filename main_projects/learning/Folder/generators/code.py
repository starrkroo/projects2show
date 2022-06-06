#!/usr/bin/env python3

jack = {
  'name': 'jack',
  'car' : 'bmv'
}

john = {
  'name': 'john',
  'car' : 'audi'
}

users = [jack,john]

cars = [person['car'] for person in users ]
print(cars)

print()

values = ['value1', 'value2', 'value3']
print([value for value in values])

print()

new = [n for n in values if n.startswith('v')]
print(new)

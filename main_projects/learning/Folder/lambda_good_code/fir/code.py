#!/usr/bin/env python3

numbers = [2, 1, 3, 4, 7, 11, 18]

# NOTE: map(что_делать, с_кем_делать
squared_numbers = list(map(lambda n: n**2, numbers)) # итерация по каждому объекту

# NOTE: filter(условие_курсора, с_работать)
# ---> формировка нового массива по условию
odd_numbers = list(filter(lambda n: n % 2 == 1, numbers)) # условие итерации

print(numbers)
print(squared_numbers)
print(odd_numbers)

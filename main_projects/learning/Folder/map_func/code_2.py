#!/usr/bin/env python3

# if you wanna use cicle for u can simmilary use map function

income = [10, 30, 75]

double_money = lambda dollars: dollars*2

print(list(map(double_money, income)))


# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів.
# На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.
from math import sin
from prettytable import PrettyTable

def square_root(arg):
    return -(abs(arg) ** 0.5) if arg < 0 else arg ** 0.5

def sinus(arg):
    return sin(arg)

x = PrettyTable()
x.field_names = ['Value', 'Root of value', 'Sinus of value']

for i in range(-5, 6):
    x.add_row([i, square_root(i), sinus(i)])
    i += 0.5

print(x)
# Напишіть програму-калькулятор, в якій користувач зможе обрати операцію,
# ввести необхідні числа та отримати результат. Операції, які необхідно реалізувати:
# додавання, віднімання, множення, ділення, зведення в ступінь, квадратний корінь, кубічний корінь,
# синус, косинус та тангенс числа.

import math

choice_operation = input("""Chooce operation: 
1.+     6.root
2.-     7.couberoot
3.*     8.sin
4./     9.cos
5.^     10.tan

Enter operation here:""")
if choice_operation == '1':
    number_1 = float(input("Enter 1st number here:"))
    number_2 = float(input("Enter 2nd number here:"))
    print(f"{number_1}+{number_2}={number_1 + number_2}")
elif choice_operation == '2':
    number_1 = float(input("Enter 1st number here:"))
    number_2 = float(input("Enter 2nd number here:"))
    print(f"{number_1}-{number_2}={number_1 - number_2}")
elif choice_operation == '3':
    number_1 = float(input("Enter 1st number here:"))
    number_2 = float(input("Enter 2nd number here:"))
    print(f"{number_1}*{number_2}={number_1 * number_2}")
elif choice_operation == '4':
    number_1 = float(input("Enter 1st number here:"))
    number_2 = float(input("Enter 2nd number here:"))
    print(f"{number_1}/{number_2}={number_1 / number_2}")
elif choice_operation == '5':
    number_1 = float(input("Enter a number here:"))
    number_2 = float(input("Enter exponantiation here:"))
    print(f"{number_1} in exp {number_2}={number_1 ** number_2}")
elif choice_operation == '6':
    number_1 = float(input("Enter a number here:"))
    print(f"Root from {number_1}={math.sqrt(number_1)}")
elif choice_operation == '7':
    number_1 = float(input("Enter a number here:"))
    print(f"Couberoot from {number_1}={number_1 ** (1 / 3)}")
elif choice_operation == '8':
    number_1 = float(input("Enter a number here:"))
    print(f"Sinus from {number_1}={math.sin(number_1)}")
elif choice_operation == '9':
    number_1 = float(input("Enter a number here:"))
    print(f"Cosinus from {number_1}={math.cos(number_1)}")
elif choice_operation == '10':
    number_1 = float(input("Enter a number here:"))
    print(f"Tan from {number_1}={math.tan(number_1)}")
else:
    print('Wrong operation')
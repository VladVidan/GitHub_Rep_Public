# Cтворіть інженерний калькулятор з використанням модуля math,
# в якому передбачене меню.
# Під час створення дотримуйтесь правил специфікації PEP 8.

import math

print("""Available Operations :
'+'
'-'
'*'
'/'
exponentiation 'exp'
square root 'squ'
cube root 'cube'
'sin'
'cos'
'exit'
""")


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


while True:
    step = input('Choose the operation : ')
    match step:
        case '+':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                print("Result =", float(number_1) + float(number_2))
            else:
                print("Wrong input!")
        case '-':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                print("Result =", float(number_1) - float(number_2))
            else:
                print("Wrong input!")
        case '*':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                print("Result =", float(number_1) * float(number_2))
            else:
                print("Wrong input!")
        case '/':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if number_2 == '0':
                print("You can't devide by zero")
            elif is_number(number_1) and is_number(number_2):
                print("Result =", float(number_1) / float(number_2))

            else:
                print("Wrong input!")
        case 'exp':
            number_1 = input('Enter number to exponentiate : ')
            number_2 = input('Enter exponantion number : ')
            if is_number(number_1) and is_number(number_2):
                if float(number_1) < 0:
                    print("Result =", -(abs(float(number_1))
                                        ** float(number_2)))
                else:
                    print("Result =", float(number_1) ** float(number_2))
            else:
                print("Wrong input!")
        case 'squ':
            number_1 = input('Enter number to find square root : ')
            if is_number(number_1):
                if float(number_1) < 0:
                    print("Result =", -(abs(float(number_1)) ** 0.5))
                else:
                    print("Result =", float(number_1) ** 0.5)
            else:
                print("Wrong input!")
        case 'cube':
            number_1 = input('Enter number to find cube root : ')
            if is_number(number_1):
                if float(number_1) < 0:
                    print("Result =", -(abs(float(number_1)) ** (1 / 3)))
                else:
                    print("Result =", float(number_1) ** (1 / 3))
            else:
                print("Wrong input!")
        case 'sin':
            number_1 = input('Enter number to find sinus : ')
            if is_number(number_1):
                print("Result =", math.sin(float(number_1)))
            else:
                print("Wrong input!")
        case 'cos':
            number_1 = input('Enter number to find cosinus : ')
            if is_number(number_1):
                print("Result =", math.cos(float(number_1)))
            else:
                print("Wrong input!")
        case 'exit':
            print("\nBye bye :)")
            break
        case other:
            print("Wrong input!")

# Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання,
# множення, ділення, зведення в ступінь, зведення до квадратного та кубічного коренів.
# Всі дані повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми.
# Кожна операція має бути реалізована у вигляді окремої функції.
# Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.

import math

print("""Available Operations :
'+'
'-'
'*'
'/'
exponentiation 'exp'
square root 'squ'
cube root 'cube'
'exit'
""")


def is_number(obj):
    try:
        float(obj)
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
                def plusing(num1,num2):
                    return print("Result =",float(num1) + float(num2))


                plusing(number_1, number_2)
            else:
                print("Wrong input!")
        case '-':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                def subtraction(num1, num2):
                    return print("Result =", float(num1) - float(num2))


                subtraction(number_1, number_2)
            else:
                print("Wrong input!")
        case '*':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if is_number(number_1) and is_number(number_2):
                def multiply(num1, num2):
                    return print("Result =", float(num1) * float(num2))


                multiply(number_1, number_2)
            else:
                print("Wrong input!")
        case '/':
            number_1 = input('Enter 1st number : ')
            number_2 = input('Enter 2nd number : ')
            if number_2 == '0':
                print("You can't devide by zero")
            elif is_number(number_1) and is_number(number_2):
                def division(num1, num2):
                    return print("Result =", float(num1) / float(num2))


                division(number_1, number_2)
            else:
                print("Wrong input!")
        case 'exp':
            number_1 = input('Enter number to exponentiate : ')
            number_2 = input('Enter exponantion number : ')
            if is_number(number_1) and is_number(number_2):
                def expon(num1, num2):
                    if float(num1) < 0:
                        return print("Result =", -(abs(float(num1)) ** float(num2)))
                    else:
                        return print("Result =", float(num1) ** float(num2))


                expon(number_1, number_2)
            else:
                print("Wrong input!")
        case 'squ':
            number_1 = input('Enter number to find square root : ')
            if is_number(number_1):
                def square_root(num1):
                    if float(num1) < 0:
                        return print("Result =", -(abs(float(num1)) ** 0.5))
                    else:
                        return print("Result =", float(num1) ** 0.5)


                square_root(number_1)
            else:
                print("Wrong input!")
        case 'cube':
            number_1 = input('Enter number to find cube root : ')
            if is_number(number_1):
                def cube_root(num1):
                    if float(num1) < 0:
                        return print("Result =", -(abs(float(num1)) ** (1 / 3)))
                    else:
                        return print("Result =", float(num1) ** (1 / 3))


                cube_root(number_1)
            else:
                print("Wrong input!")
        case 'exit':
            print("\nBye bye :)")
            break
        case other:
            print("Wrong input!")










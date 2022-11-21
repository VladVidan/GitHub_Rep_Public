# Створіть програму, яка приймає як формальні параметри зріст і вагу користувача, обчислює індекс
# маси тіла і в залежності від результату повертає інформаційне повідомлення
# (маса тіла в нормі, недостатня вага або слідкуйте за фігурою). Користувач з клавіатури вводить значення росту та
# маси тіла та передає ці дані у вигляді фактичних параметрів під час виклику функції.
# Програма працює доти, доки користувач не зупинить її комбінацією символів «off».

def body_index(height, weight):
    i = weight / ((height / 100) ** 2)
    if i < 18.5:
        return "You are underweight!"
    elif 18.5 <= i < 25:
        return "Your weight is normal"
    elif 25 <= i < 40:
        return "You are overweight"
    elif i >= 40:
        return "Oh! You are so fat!"

def is_number(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False


while True:
    height = input("Enter your height, or 'off' to quit :")
    if height == 'off':
        break
    weight = input("Enter your weight :")
    if is_number(height) & is_number(weight):
        print('\n',body_index(float(height), float(weight)), '\n')



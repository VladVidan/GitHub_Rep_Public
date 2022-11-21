# Створіть програму, яка складається з функції, яка приймає три числа і повертає їх середнє арифметичне,
# і головного циклу, що запитує у користувача числа і обчислює їх середні значення за допомогою створеної функції.

def average_use_str(num1, num2, num3):
    return (float(num1) + float(num2) + float(num3)) / 3

def is_number(obj):
    try:
        float(obj)
        return True
    except ValueError:
        return False

while True:
    num1 = input("Enter number 1 :")
    num2 = input("Enter number 2 :")
    num3 = input("Enter number 3 :")
    if is_number(num1) & is_number(num2) & is_number(num3):
        print(f"Average is : {average_use_str(num1, num2, num3)}")
    else:
        print("Wrong input! Try again!")
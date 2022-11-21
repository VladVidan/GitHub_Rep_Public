# Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел
# (в діапазоні має бути не менше 5 чисел).
# Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної послідовності.

while True:
    range_from = input("Range from :")
    range_to = input("To :")
    if range_from.isdigit() and range_to.isdigit():
        range_list = list(range(int(range_from), int(range_to) + 1))
        if len(range_list) >= 5:
            print(f'Second number is {range_list[1]}')
            print(f'Pre-last number is {range_list[-2]}')
            print(f'Avarage of range is {sum(range_list) / len(range_list)}')
            break
        else:
            print("Range should more then 5! Try again!")
    else:
        print("Range data should be a digit! Try again!")
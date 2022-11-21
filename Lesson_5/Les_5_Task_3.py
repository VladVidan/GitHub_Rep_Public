# Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору)
# у форматі RGB і виводить на екран кортеж, у якому зберігається колір.

while True:
    red_portion = input("Enter Red portion :")
    green_portion = input("Enter Green portion :")
    blue_portion = input("Enter Blue portion :")

    list_for_check = [red_portion, green_portion, blue_portion]
    list_result = []
    for i in list_for_check:
        if len(i) == 0:
            print("You can't skip any input! Try again!")
            break
        elif i.isdigit() == False:
            print('Colors portion should be a digits from 0 to 255! Try again!')
            break
        elif int(i) not in range(0, 256):
            print('Colors portion should be a digits from 0 to 255! Try again!')
            break
        else:
            list_result.append(int(i))
    if len(list_for_check) == len(list_result):
        r, g, b = list_result
        result_tuple = r, g, b
        print(f"Your color set include \n R:{result_tuple[0]} \n G:{result_tuple[1]} \n B:{result_tuple[2]}")
        break
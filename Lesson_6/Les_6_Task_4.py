# Створіть список, введіть кількість його елементів і самі значення. Передбачити меню, в якому: після натискання
# клавіші 1 ці значення виведуться на екран у зворотному порядку, а після натискання клавіші 2 – за зростанням.

some_list = [1, 4, 7, -5, 0, 16, 14]

while True:
    operation_for_list = input("Select an operation for list\n1.Reverse\n2.Sort Ascending\nEnter here :")
    if operation_for_list == '1':
        print(some_list[::-1])
        break
    elif operation_for_list == '2':
        print(sorted(some_list))
        break
    else:
        print("Wrong enter! Try again!")
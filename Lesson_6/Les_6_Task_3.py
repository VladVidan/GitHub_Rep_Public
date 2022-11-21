# Простим називається число, яке ділиться націло лише на одиницю і на саме себе. Число 1 не вважається простим.
# Напишіть програму, яка знаходить усі прості числа в заданому проміжку, виводить їх на екран,
# а потім на вимогу користувача виводить їхню суму або добуток.

import sympy
import math

random_numbers_list = [-3, 'obj', 1, 67, 13, 22, 0, 14, 7]
result_list = []
for i in random_numbers_list[2::]:
    if sympy.isprime(i) == True:
        result_list.append(i)

print(F'Prime numbers is : {result_list}')

while True:
    operation_for_list = input("Select an operation for Prime numbers\n1.Sum\n2.Product\nEnter here :")
    if operation_for_list == '1':
        print(sum(result_list))
        break
    elif operation_for_list == '2':
        print(math.prod(result_list))
        break
    else:
        print("Wrong enter! Try again!")
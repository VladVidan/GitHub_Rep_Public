

import math
import random
from math import pi, e

some_print = 5
repeat_count = int(input('Введите количество повторов :'))
print(some_print * repeat_count)
print(pi * (some_print * repeat_count))
print(e * 2)
while some_print >= 0:
    some_print -= 1
my_str = 'my string'
some_sum = 0
for elem in my_str:
    some_sum += pow(my_str.find(elem), 2)
    print("sum=", some_sum)


def my_func(atr=1):
    print('atr', atr)


print(my_func(atr=5))

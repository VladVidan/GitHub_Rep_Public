# Напишіть програму, яка вводить з клавіатури послідовність чисел,
# перетворює послідовність на кортеж і виводить його відсортованим у порядку зростання.

list_input = input('Input numbers here :')
tuple_for_sort = tuple(sorted(list_input))
print(tuple_for_sort)
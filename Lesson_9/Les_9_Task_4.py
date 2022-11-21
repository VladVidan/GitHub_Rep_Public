# Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.

def sum_of_nat_num(num_from, num_to) -> int:
    if num_to == num_from:
        return num_from
    return sum_of_nat_num(num_from, num_to - 1) + num_to


print(sum_of_nat_num(2, 4))
# Створіть список та введіть його значення.
# Знайдіть найбільший та найменший елемент списку, а також суму та середнє арифметичне його значень.
import statistics

some_list = [1, 2, -3, -15, 29, -101, 0, 74]
print(f'Max value of the list : {max(some_list)}')
print(f'Min value of the list : {min(some_list)}')
print(f'Sum of the list is : {sum(some_list)}')
print(f'Average of the list : {statistics.mean(some_list)}')

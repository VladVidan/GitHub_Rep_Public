# Створіть програму, яка має 2 списки цілочисельних значень
# та друкує список унікальних значень без повтору, які є в 1 списку (немає в другому) і навпаки.

list_1 = [1, 2, 3, 5, 7, 9, 12, 4, 2, 6]
list_2 = [5, 58, 5, 14, 12, 3, 9, 9]

print("Unique symbols of 1st list:", set(list_1) - (set(list_2)))
print("Unique symbols of 2nd list:", set(list_2) - (set(list_1)))

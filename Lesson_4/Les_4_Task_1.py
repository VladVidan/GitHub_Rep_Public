# Дано числа a і b (a < b). Виведіть суму всіх натуральних чисел від a до b (включно).

a = 1
b = 10
result = 0
for i in range(a, b + 1):
    result += i
print(result)
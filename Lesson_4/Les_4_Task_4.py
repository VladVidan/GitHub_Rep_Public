# Дано числа a і b (a < b). Виведіть на екран суму всіх натуральних чисел
# від a до b (включно), які є кратними середньому арифметичному цього проміжку.

print("Integer 'a' should be smaler then 'b'")
while True:
    a = int(input("Enter integer 'a' here :"))
    b = int(input("Enter integer here :"))
    if a < b:
        break
    else:
        print("Wrong numbers , integer 'a' should be smaler then 'b'!")

list_for_avarage = []
for i in range(a, b + 1):
    list_for_avarage.append(i)
avarage = sum(list_for_avarage) / len(list_for_avarage)

result = 0
for i in list_for_avarage:
    if i % avarage == 0:
        result += i
print(result)




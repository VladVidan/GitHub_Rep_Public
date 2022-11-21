# Прочитайте у документації з мови Python інформацію про перелічені у резюме цього уроку стандартні функції.
# Перевірте їх на практиці.

# abs(x) – модуль числа x
print(abs(5))
print(abs(-6))

# bin(x) – подання числа x у двійковій системі числення
print(bin(10))
print(bin(-2))

# bool(x) – створити значення типу bool із x
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool('string'))
print(bool(''))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(None))

# callable(f) – перевірити, чи можна викликати f як функцію
def func():
    return 1

x = 123
print(callable(func))
print(callable(x))

# chr(code) – символ із кодом code
print(chr(1))
print(chr(55))

# complex(real, imag) – створити комплексне число
print(complex(5))

# dir(obj) – вивести список полів та методів об'єкту obj
abc = 5
print(dir(abc))

# float(x) – створити дійсне число з x
print(float(5))
print(float(-10))
print(float(0))
print(float(55.5))

# format(x, fmt) – повертає рядок, що представляє значення x, відформатоване відповідно до форматного рядка fmt
print("I am {name}".format(name="Vlad"))

# help(obj) – виводить довідку по об'єкту obj
ggg = 3
help(ggg)
help(str)
help(float)

# hex(x) – шістнадцяткове представлення числа x
print(hex(5))

# id(obj) – значення, унікальне для кожного об'єкта (у CPython – адреса об'єкта в пам'яті)
some_str = 'blablabla'
print(id(some_str))
print(id(5))
print(id(print))

# input() – введення даних
###i nput_name = input("Enter your name")
### print(input_name)

# int(x) – створити ціле число
print(int(5.0))
print(int(-50.0))

# len(s) – довжина рядка або будь-якої іншої послідовності
print(len('abc'))
print(len((1, 2, 3, 4, 5, 6)))

# max(arg1, arg2, …) – максимальне число серед заданих
print(max(1, 4, -5, 16, 3))

# min(arg1, arg2, …) – мінімальне число серед заданих
print(min(1, 4, -5, 16, 3))


# oct(x) – подання числа x у восьмеричній системі числення
print(oct(10))
print(oct(-25))

# ord(c) – код символу c
print(ord('a'))
print(ord('t'))

# pow(x, n) – число x у ступені n
print(pow(2, 3) == 2 ** 3)

# print() – виведення даних
print('Here is your print')

# range() – послідовність цілих чисел (див. урок про цикли)
for i in range(11):
    print(i)

for i in range(10, 1, -2):
    print(i)

# repr(obj) – рядкове представлення об'єкта
print(repr("""a
b
c
"""))

# reversed(iterable) – обхід послідовності у зворотному порядку
iter_check = 'Python'
print(list(reversed(iter_check)))

# round(number, ndigits) – округлення числа (в случае c ровной дробью(.5) округляет до ближайшего четного числа
print(round(2.9))
print(round(1.3))
print(round(2.5))
print(round(3.5))

# sorted(iterable) – сортує послідовність у порядку зростання чи спадання значень
print(sorted('gdkgalwg'))
print(sorted([9, 4, 1, 7, 3]))
print(sorted([9, 4, 1, 7, 3], reverse=True)) #в обратном порядке

# str(x) – створення рядка з x
print(str(333))
print(str(2.5))

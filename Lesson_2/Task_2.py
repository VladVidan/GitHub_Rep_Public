 #Напишіть програму, яка запитує три цілі числа a, b і x та друкує їх добуток.

while True:
    a = input('Please, enter 1st number here :')
    if a.isdigit():
        print('Nice job')
        break
    else:
        print('Wrong symbols! Please, enter 1st number here :')

while True:
    b = input('Please, enter 2nd number here :')
    if a.isdigit():
        print('Nice job')
        break
    else:
        print('Wrong symbols! Please, enter 2nd number here :')

while True:
    x = input('Please, enter 3rd number here :')
    if a.isdigit():
        print('Nice job')
        break
    else:
        print('Wrong symbols! Please, enter 3rd number here :')

print(f'Sum is : {int(a) + int(b) + int(x)}')

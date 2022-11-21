# Напишіть програму, в якій користувач вводить фразу з клавіатури, яка складається з 10 символів.
# На екрані виведіть суму ASCII-кодів символів введеного рядка.
# Не понял нужен перечень ASCII строки или сумма , тут перечень :

while True:
    tenSymbolsRequest = input('Please, enter 10 symbols here :')
    if len(tenSymbolsRequest) == 10:
        break
    else:
        print('Wrong string lenght')

result = []
for i in tenSymbolsRequest:
    result.append(ord(i))
print(f'Your ASCII list : {result}')
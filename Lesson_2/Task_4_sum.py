# Напишіть програму, в якій користувач вводить фразу з клавіатури, яка складається з 10 символів.
# На екрані виведіть суму ASCII-кодів символів введеного рядка.

tenSymbolsRequest = input('Enter 10 symbols :')
print(sum(map(ord, tenSymbolsRequest)))
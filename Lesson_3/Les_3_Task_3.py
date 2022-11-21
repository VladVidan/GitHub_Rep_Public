# Напишіть програму, яка розв'язує квадратне рівняння 𝑎𝑥 2 + 𝑏𝑥 + 𝑐 = 0 у дійсних числах.
# С учетом дискриминанта

while True:
    a = float(input('Enter a number(except 0) = '))
    if a != 0:
        break
    else:
        print('You can not use 0 in a')

b = float(input('Enter b number = '))
c = float(input('Enter c number = '))

Discrim = b ** 2 - (4 * a * c)

if Discrim > 0:
    x1 = (-b) + (Discrim ** 0.5) / (2 * a)
    x2 = (-b) - (Discrim ** 0.5) / (2 * a)
    print(f'x1 = {x1} and x2 = {x2}')
elif Discrim == 0:
    x = (-b) / (2 * a)
    print(f'x = {x}')
else:
    print('It is no roots')

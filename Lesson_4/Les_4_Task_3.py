# Використовуючи вкладені цикли та функції
# print(‘*’, end=’’), print(‘ ‘, end=’’) та print() виведіть на екран прямокутний трикутник


# Метод по условию :
for i in range(15):
    for x in range(i):
        print('*', end='')
        print(' ', end='')
    print()

# Метод который первый пришел в голову (помоему проще)
for i in range(15):
    print(i * '* ', end='\n')

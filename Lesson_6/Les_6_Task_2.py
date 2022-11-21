# Є два списки, які наповнюються користувачем з клавіатури.
# Сформувати список, в якому будуть міститися унікальні значення першого відносно другого списку та навпаки без повторень.
# Роздрукувати підсумковий
# об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.

list_1 = list(input("Enter parts of list 1 :"))
list_2 = list(input("Enter parts of list 2 :"))

result_list = list(set(list_1) ^ set(list_2))
print(f'Straight print :{result_list}')
print(f'Reversed print :{result_list[::-1]}')
print(f'Sort ascending :{sorted(result_list)}')
print(f'Sort descending :{sorted(result_list, reverse=True)}')




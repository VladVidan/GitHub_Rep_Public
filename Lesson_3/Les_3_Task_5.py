#  Напишіть програму для перевірки введеного числа на ознаку парності.
#  Якщо число парне/непарне – вивести відповідне повідомлення на екран.
#  Для опису цього алгоритму використовувати тернарний оператор.

number_for_check = int(input("Enter number here :"))
print("Chet") if number_for_check % 2 == 0 else print("Ne chet")
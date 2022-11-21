# Дано два рядки. Виведіть на екран символи, які є в обох рядках.

str_1 = input("Enter 1st string :")
str_2 = input("Enter 2nd string :")
print(set(str_1).intersection(str_2))

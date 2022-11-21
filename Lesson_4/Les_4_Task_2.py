# Факторіалом числа n називається число n!=1∙2∙3∙…∙n.
# Створіть програму, яка обчислює факторіал введеного користувачем числа.

test_number = int(input("Enter number here :"))
factorial_of_test_number = 1
for i in range(1, test_number + 1):
    factorial_of_test_number *= i
print(factorial_of_test_number)
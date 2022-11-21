# Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє,чи складається
# рядок з літер, при чому кожне слово має бути записане з великої літери. Вивести результат на екран.

print("Enter your last, fathers and regular names only with title words")
while True:
    initials = input("Enter your data here :")
    if initials.istitle():
        second_check = initials.replace(' ', '')
        if second_check.isalpha():
            print(f"Nice job {initials}!")
            break
    else:
        print("Try again!")

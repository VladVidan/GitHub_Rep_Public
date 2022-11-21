# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

polindrome = 'Race car'
not_polindrome = 'What u want?'

def is_polindrome(string: str) -> bool:
    result = string.replace(' ', '')
    return result.lower() == result.lower()[::-1]


print(is_polindrome(polindrome))
print(is_polindrome(not_polindrome))

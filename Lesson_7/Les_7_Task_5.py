# Є рядок, в якому зберігаються 1000 слів. Створіть словник із ключами - унікальними словами
# та значеннями - кількістю повторів кожного слова у послідовності.

some_string = "Any bany any bom bom " * 200
result = dict()

for word in some_string.lower().split():
    if word not in result.keys():
        result[word] = 1
    else:
        result[word] += 1

print(result)

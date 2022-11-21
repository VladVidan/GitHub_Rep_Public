# Нехай на кожну сходинку можна стати з попередньої або переступивши через одну.
# Визначте, скількома способами можна піднятися на задану сходинку.

stairs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def count_of_ways(arg) -> str:
    return 'You have two ways' if arg in stairs_list[1::2] else 'You have the only way'


print(count_of_ways(5))


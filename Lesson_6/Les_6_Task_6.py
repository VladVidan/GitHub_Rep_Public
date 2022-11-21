# Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5.
# Користувач вводить з клавіатури значення;
# якщо таке є у цьому списку — вивести кількість його повторів та його позицію у цьому списку.


new_list_x2 = [3, 17, 9, 5, 3, 3, 17, 9, 5, 3]
position_list = []
element_repeat_times = 0
symb_check = int(input("Enter number for find in new_list :"))

if symb_check not in new_list_x2:
    print(f"There is no {symb_check} in new_list!")
else:
    for index, elem in enumerate(new_list_x2):
        if elem == symb_check:
            element_repeat_times += 1
            position_list.append(index + 1)
    print(element_repeat_times)
    print(position_list)




# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін
# за структурою: автор: твір.Передбачте можливість виведення на екран сортування за автором та твором.

library_base = {
    'Xavier': ['Night Winters', 'The Patriot'],
    'Andersen': ['Road To Mars'],
    'Roling': ['Harry Potter'],
}
while True:
    add_or_show = input("Select the operation:\n1.Add new book.\n2.Show sorted library\n")
    if add_or_show == '1' or 'add' in add_or_show.lower():
        new_author = input("Enter name of author here :")
        new_book = input("Enter the name of authors book :")
        library_base[new_author] = [new_book]
    elif add_or_show == '2' or 'show' in add_or_show.lower():
        sort_by = input("Sort by:\n1.Name of author\n2.Name of books\n")
        if sort_by == '1' or 'aut' in sort_by.lower():
            print(dict(sorted(library_base.items())))
            break
        elif sort_by == '2' or 'book' in sort_by.lower():
            print(dict(sorted(library_base.items(), key=lambda item: item[1])))
            break
        else:
            print('Wrong input!\nPlease, try again :)\n')
    else:
        print('Wrong input!\nPlease, try again :)\n')

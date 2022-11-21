# Створіть програму, яка емулює роботу сервісу зі скорочення посилань. Повинна бути реалізована
# можливість введення початкового посилання та короткої назви і отримання початкового посилання за її назвою.

links_dict = {
    'fb': 'www.facebook.com',
    'insta': 'www.instagram.com',
    'li': 'www.linkedin.com',
}

user_search = input('What you looking for? :')

if user_search.lower() in links_dict.keys():
    print(f"Loading...{links_dict[user_search]}")
else:
    user_answer = input("""Can't find this web-site :(\nDo you want to add new one?
1.Yes\n2.No\n""")

    if user_answer.lower() == 'yes' or user_answer.lower() == '1':
        new_key = input("Enter new keyword for website :")
        new_site = input("Enter full name of website :")
        links_dict[new_key] = new_site
        print("Well done! Check new update :\n", links_dict)
    elif user_answer.lower() == 'no' or user_answer.lower() == '2':
        print("OK! Bye bye :)")
    else:
        print('Wrong input , bye bye!')

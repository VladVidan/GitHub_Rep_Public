# Напишіть програму для аналізу фідбеку від відвідувачів курорту
# «Морська зірка», яка повинна знаходити згадки про меню, спортзал, обслуговування.
# Якщо фідбек перевищив 60 символів, відвідувачу надається знижка 15% на наступне відвідування.

from collections import namedtuple

feedback = namedtuple('Feedback', 'Guest Menu GYM Service Comment')
review_account = feedback('Guest', 'Menu', 'GYM', 'Service', 'Comment')
input_name = input("Input your name :")
review_account = review_account._replace(Guest=input_name)
menu_grade = input('Rate the menu from 1 to 5 :')
review_account = review_account._replace(Menu=menu_grade)
gym_grade = input('Rate the GYM from 1 to 5 :')
review_account = review_account._replace(GYM=gym_grade)
service_grade = input('Rate the service from 1 to 5 :')
review_account = review_account._replace(Service=service_grade)
comment = input("Write a general impression about 'Sea Star' :")
review_account = review_account._replace(Comment=comment)

if len(comment) >= 60:
    print(review_account)
    print('Thanks for your feedback , your discount is 15%')
else:
    print(review_account)
    print('Thanks for your feedback!')





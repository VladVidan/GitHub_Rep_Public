# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections.
# Створіть фабрику іменованих кортежів оцінок для учнів однієї групи з предметів:
# алгебра, геометрія, історія, інформатика, географія. Вивести дані на екран.

from collections import namedtuple, deque

student_info = namedtuple('student_info', 'name algebra geometry history computer_science geography')

vlad = student_info('Vlad', 4, 3, 5, 5, 4)
lily = student_info('Lily', 5, 5, 4, 2, 5)
mark = student_info('Mark', 2, 2, 3, 4, 3)

group_of_students = deque([vlad, lily, mark], maxlen=3)
print(*group_of_students, sep='\n')
print("It's your students!")

inokentiy = student_info('Inokentiy', 5, 5, 3, 2, 1)
group_of_students.append(inokentiy)
print(*group_of_students, sep='\n')
print("It's your students!")

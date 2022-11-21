# Написати програму визначення днів тижня. Дані про день тижня вводяться користувачем з клавіатури.
# Якщо будній день - виводити на екран повідомлення "Сьогодні на роботу", у вихідні дні - "Сьогодні вихідний",
# в інших випадках - "Такого дня не існує".

input_day = input("Введите день недели :")
workdays_list = ["понедельник", "вторник", "среда", "четверг", "пятница"]
weekdays_list = ["суббота", "воскресенье"]

if input_day.lower() in workdays_list:
    print("Газуй на работу")
elif input_day.lower() in weekdays_list:
    print("Поваляйся на диване сегодня")
else:
    print("Нет такого дня недели")
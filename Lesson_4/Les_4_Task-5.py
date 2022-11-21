# Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини та висоти.

while True:
    rectangle_width = int(input("Enter rectangle width :"))
    rectangle_hight = int(input("Enter rectangle hight :"))
    if rectangle_hight != rectangle_width:
        break
    else:
        print("You drawing a rectangle , not a square :)")

for i in range(rectangle_hight):
    print(rectangle_width * '* ', end='\n')

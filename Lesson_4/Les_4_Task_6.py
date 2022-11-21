# Створіть програму авторизації, в якій користувачеві дається 3 спроби ввести
# свої облікові дані (логін та пароль). Якщо користувач за меншу кількість спроб ввів вірні дані,
# програма достроково припиняє своє виконання та виводить на екран
# повідомлення: «Авторизацію успішно пройдено з «№» спроби».

print('Registration first')
login_reg = input('Enter registration login here :')
password_reg = input('Enter registration password here :')
client_account = login_reg + password_reg

print('Now - autorization')
for i in range(1, 4):
    login_check = input('Enter your login :')
    password_check = input('Enter your password :')
    autorization_result = login_check + password_check
    if autorization_result == client_account:
        print(f'Succes autorization with {i} try!:)')
        break
    else:
        print('Wrong account data!')

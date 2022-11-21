# Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін
# до структури(реалізуйте інтерфейс(меню), за допомогою якого можна робити маніпуляції з даними):
# прізвище:
#     посада: ...
#     досвід роботи: …
#     портфоліо: …
#     коефіцієнт ефективності: …
#     стек технологій: …
#     зарплата: …
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.

from collections import ChainMap
from operator import itemgetter


all_stuff_info = ChainMap(
{'name': 'Vlad','job title': 'boss', 'experience years': '7', 'portfolio grade': '5',
'efficiency ratio': '0.9', 'technology stack': 'team-lead', 'salary': '6300'},
{'name': 'Lily','job title': 'designer', 'experience years': '3', 'portfolio grade': '3',
'efficiency ratio': '0.85', 'technology stack': 'ui/ux', 'salary': '2800'},
{'name': 'Poroshenko','job title': 'cleaner', 'experience years': '4', 'portfolio grade': '0',
'efficiency ratio': '1', 'technology stack': 'dry cleaning', 'salary': '25000'},
)

while True:
    first_step_menu = input('Choose an operation:\n1.Show stuff info\n2.Change stuff info\nEnter :')
    if first_step_menu == '1' or 'sho' in first_step_menu.lower():
        show_info_choice = input("""How do you want to display stuff info?
1.View general list\n2.View sorted by name\n3.View sorted by efficiency ratio\nEnter :""")
        if show_info_choice == '1' or 'gen' in show_info_choice.lower():
            for d in all_stuff_info.maps:
                print(sep='\n')
                for k, v in d.items():
                    print(k, v, sep=' -> ')
            break
        elif show_info_choice == '2' or 'name' in show_info_choice.lower():
            for d in sorted(all_stuff_info.maps, key=itemgetter('name')):
                print(sep='\n')
                for k, v in d.items():
                    print(k, v, sep=' -> ')
            break
        elif show_info_choice == '3' or 'effic' in show_info_choice.lower():
            for d in sorted(all_stuff_info.maps, key=itemgetter('efficiency ratio')):
                print(sep='\n')
                for k, v in d.items():
                    print(k, v, sep=' -> ')
            break
        else:
            print('Wrong input! Try again :)')
    elif first_step_menu == '2' or 'chan' in first_step_menu.lower():
        change_info_choice = input('Choose an employee:\n1.Vlad\n2.Lily\n3.Poroshenko\nEnter :')
        if change_info_choice == '1' or 'vlad' in change_info_choice.lower():
            section_to_change = input("""Choose a section to change:\n1.Name\n2.Job title\n3.Experience years
4.Portfolio grade\n5.Efficiency ratio\n6.Technology stack\n7.Salary\nEnter :""")
            if section_to_change == '1' or 'name' in section_to_change.lower():
                new_name = input('Enter a new name :')
                list(all_stuff_info.maps)[0]['name'] = new_name
            elif section_to_change == '2' or 'job' in section_to_change.lower():
                new_job_title = input('Enter a new job title :')
                list(all_stuff_info.maps)[0]['job title'] = new_job_title
            elif section_to_change == '3' or 'exp' in section_to_change.lower():
                new_exp_years = input('Enter a new experience years :')
                list(all_stuff_info.maps)[0]['experience years'] = new_exp_years
            elif section_to_change == '4' or 'portf' in section_to_change.lower():
                new_portfolio_grage = input('Enter a new portfolio grade :')
                list(all_stuff_info.maps)[0]['portfolio grade'] = new_portfolio_grage
            elif section_to_change == '5' or 'effi' in section_to_change.lower():
                new_efficiency = input('Enter a new efficiency ratio :')
                list(all_stuff_info.maps)[0]['efficiency ratio'] = new_efficiency
            elif section_to_change == '6' or 'techno' in section_to_change.lower():
                new_tech_stack = input('Enter a new technology stack :')
                list(all_stuff_info.maps)[0]['technology stack'] = new_tech_stack
            elif section_to_change == '7' or 'sala' in section_to_change.lower():
                new_salary = input('Enter a new salary :')
                list(all_stuff_info.maps)[0]['salary'] = new_salary
            else:
                print('Wrong input! Try again :)')
        elif change_info_choice == '2' or 'lily' in change_info_choice.lower():
            section_to_change = input("""Choose a section to change:\n1.Name\n2.Job title\n3.Experience years
4.Portfolio grade\n5.Efficiency ratio\n6.Technology stack\n7.Salary\nEnter :""")
            if section_to_change == '1' or 'name' in section_to_change.lower():
                new_name = input('Enter a new name :')
                list(all_stuff_info.maps)[1]['name'] = new_name
            elif section_to_change == '2' or 'job' in section_to_change.lower():
                new_job_title = input('Enter a new job title :')
                list(all_stuff_info.maps)[1]['job title'] = new_job_title
            elif section_to_change == '3' or 'exp' in section_to_change.lower():
                new_exp_years = input('Enter a new experience years :')
                list(all_stuff_info.maps)[1]['experience years'] = new_exp_years
            elif section_to_change == '4' or 'portf' in section_to_change.lower():
                new_portfolio_grage = input('Enter a new portfolio grade :')
                list(all_stuff_info.maps)[1]['portfolio grade'] = new_portfolio_grage
            elif section_to_change == '5' or 'effi' in section_to_change.lower():
                new_efficiency = input('Enter a new efficiency ratio :')
                list(all_stuff_info.maps)[1]['efficiency ratio'] = new_efficiency
            elif section_to_change == '6' or 'techno' in section_to_change.lower():
                new_tech_stack = input('Enter a new technology stack :')
                list(all_stuff_info.maps)[1]['technology stack'] = new_tech_stack
            elif section_to_change == '7' or 'sala' in section_to_change.lower():
                new_salary = input('Enter a new salary :')
                list(all_stuff_info.maps)[1]['salary'] = new_salary
            else:
                print('Wrong input! Try again :)')
        elif change_info_choice == '3' or 'poroshenko' in change_info_choice.lower():
            section_to_change = input("""Choose a section to change:\n1.Name\n2.Job title\n3.Experience years
4.Portfolio grade\n5.Efficiency ratio\n6.Technology stack\n7.Salary\nEnter :""")
            if section_to_change == '1' or 'name' in section_to_change.lower():
                new_name = input('Enter a new name :')
                list(all_stuff_info.maps)[2]['name'] = new_name
            elif section_to_change == '2' or 'job' in section_to_change.lower():
                new_job_title = input('Enter a new job title :')
                list(all_stuff_info.maps)[2]['job title'] = new_job_title
            elif section_to_change == '3' or 'exp' in section_to_change.lower():
                new_exp_years = input('Enter a new experience years :')
                list(all_stuff_info.maps)[2]['experience years'] = new_exp_years
            elif section_to_change == '4' or 'portf' in section_to_change.lower():
                new_portfolio_grage = input('Enter a new portfolio grade :')
                list(all_stuff_info.maps)[2]['portfolio grade'] = new_portfolio_grage
            elif section_to_change == '5' or 'effi' in section_to_change.lower():
                new_efficiency = input('Enter a new efficiency ratio :')
                list(all_stuff_info.maps)[2]['efficiency ratio'] = new_efficiency
            elif section_to_change == '6' or 'techno' in section_to_change.lower():
                new_tech_stack = input('Enter a new technology stack :')
                list(all_stuff_info.maps)[2]['technology stack'] = new_tech_stack
            elif section_to_change == '7' or 'sala' in section_to_change.lower():
                new_salary = input('Enter a new salary :')
                list(all_stuff_info.maps)[2]['salary'] = new_salary
            else:
                print('Wrong input! Try again :)')
        else:
            print('Wrong input! Try again :)')
    else:
        print('Wrong input! Try again :)')
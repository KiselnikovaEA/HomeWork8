import csv

def show_csv():
    with open('employees.csv', 'r', encoding='utf-8-sig') as em:
        reader = csv.DictReader(em, delimiter=',')
        for row in reader:
                print(f'Фамилия: {row["Фамилия"]}\nИмя: {row["Имя"]}\nДолжность: {row["Должность"]}\nОтдел: {row["Отдел"]}\nТелефон: {row["Телефон"]}\n')           

def find_entry_last_name(attr):
    with open('employees.csv', 'r', encoding='utf-8-sig') as em:
        reader = csv.DictReader(em, delimiter=',')
        for row in reader:
            if row["Фамилия"] == attr:
                print(f'Фамилия: {row["Фамилия"]}\nИмя: {row["Имя"]}\nДолжность: {row["Должность"]}\nОтдел: {row["Отдел"]}\nТелефон: {row["Телефон"]}\n')

def find_entry_job_title(attr):
    with open('employees.csv', 'r', encoding='utf-8-sig') as em:
        reader = csv.DictReader(em, delimiter=',')
        for row in reader:
            if row["Должность"] == attr:
                print(f'Фамилия: {row["Фамилия"]}\nИмя: {row["Имя"]}\nДолжность: {row["Должность"]}\nОтдел: {row["Отдел"]}\nТелефон: {row["Телефон"]}\n')

def find_entry_department(attr):
    with open('employees.csv', 'r', encoding='utf-8-sig') as em:
        reader = csv.DictReader(em, delimiter=',')
        for row in reader:
            if row["Отдел"] == attr:
                print(f'Фамилия: {row["Фамилия"]}\nИмя: {row["Имя"]}\nДолжность: {row["Должность"]}\nОтдел: {row["Отдел"]}\nТелефон: {row["Телефон"]}\n')

def write_entry(entry):
    attrs = ['Фамилия', 'Имя', 'Должность', 'Отдел', 'Телефон']
    dct = {attr: meaning for attr, meaning in zip(attrs, entry)}
    with open('employees.csv', 'a', encoding='utf-8-sig') as sh:
        writer = csv.DictWriter(sh, delimiter=',', fieldnames=attrs, lineterminator='\n')
        writer.writerow(dct)
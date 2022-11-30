def choose_mode(): # working_mode_input
    mode = input('Выберите режим работы:\n1 - Просмотр данных\n2 - Найти запись\n3 - Новая запись\nq - выход\n')
    return mode

def choose_attribute():
    attr = input('Поиск по атрибуту:\n1 - Фамилия\n2 - Должность\n3 - Отдел\n')
    return attr

def error_message():
    print('Ошибка')

def choose_entry():
    attr = input('Поиск записи: ')
    return attr

def entry_inp():
    entry = [input('Фамилия: '), input('Имя: '), input('Должность: '), input('Отдел: '), input('Телефон: ')]
    return entry

def end_message():
    print('Работа завершена')

def writing_complete_message():
    print('Запись создана')
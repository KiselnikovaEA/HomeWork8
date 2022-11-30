import model
import view

def button_click():
    while True:
        wtd = view.choose_mode() # what to do | 1, 2, 3, q
        if wtd == '1': # Просмотр данных
            model.show_csv()
        elif wtd == '2': # Найти запись
            hts = view.choose_attribute() # how to search | 1, 2, 3
            if hts == '1': # Найти запись по полю "Фамилия"
                entry = view.choose_entry()
                model.find_entry_last_name(entry)
            elif hts == '2': # Найти запись по полю "Должность"
                entry = view.choose_entry()
                model.find_entry_job_title(entry)
            elif hts == '3': # Найти запись по полю "Отдел"
                entry = view.choose_entry()
                model.find_entry_department(entry)
            else:
                view.error_message()
        elif wtd == '3': # Новая запись
            wtw = view.entry_inp() # what to write | Список
            model.write_entry(wtw)
            view.writing_complete_message()
        elif wtd == 'q':
            view.end_message()
            break
        else:
            view.error_message()
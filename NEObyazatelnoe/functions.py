# ЗАДАЧА 1, 2. 
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.

# def num_translate_adv(num):
#     numbers = {
#             'zero': 'ноль',
#             'one': 'один',
#             'two': 'два',
#             'three': 'три',
#             'four': 'четыре',
#             'five': 'пять',
#             'six': 'шесть',
#             'seven': 'семь',
#             'eight': 'восемь',
#             'nine': 'девять',
#             'ten' : 'десять'
#             }

#     if num.istitle():
#         return numbers[num.lower()].title()
#     else:
#         return(numbers[num])
        
# str_num = input('Введите число [zero, nine] в строку: ') # string
# print(num_translate_adv(str_num))

# ЗАДАЧА 3. -----------------------------------------------------------------------------------------------------------------------------------------------
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например: thesaurus("Иван", "Мария", "Петр", "Илья")
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
# Ответ: Если нужна сортировка по ключам, то её можно сделать в созданном списке списке first_letter, а потом уже формировать словарь my_dict

# def thesaurus(*names):
#     first_letter = [name[0] for name in names]
#     # first_letter.sort()
#     my_dict = {a: list() for a in first_letter}
#     for name in names:
#         my_dict[name[0]].append(name)
#     return my_dict

# print(thesaurus("Мария", "Петр", "Илья", "Иван"))

# ЗАДАЧА 4* Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, --------------------
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.

# def thesaurus_adv(*names):
#     first_letter_surname = [name.split()[-1][0] for name in names]
#     first_letter_surname.sort()
#     main_dict = dict.fromkeys(first_letter_surname)

#     for entry in main_dict:
#         first_letter_name = [name.split()[0][0] for name in names if name.split()[-1][0] == entry]
#         my_dict = {a: list() for a in first_letter_name}
#         for name in names:
#             if name.split()[0][0] in my_dict and name.split()[-1][0] == entry:
#                 my_dict[name.split()[0][0]].append(name)
#         main_dict[entry] = my_dict
#     return main_dict
    
# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
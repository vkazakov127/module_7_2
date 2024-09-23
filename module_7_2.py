# -*- coding: utf-8 -*-
# module_7_2.py
import io
from pprint import pprint


def custom_write(file_name: str, strings: list):
    strings_positions = {}  # Словарь на выход
    with open(file_name, mode='w', encoding='utf8') as file:
        for line in strings:
            file_position = file.tell()  # Позиция строки в файле, в байтах
            file.write(line+'\n')  # Записываем в файл
            line_number = strings.index(line) + 1  # Номер строки в списке "strings"
            # Записываем в "Словарь на выход"
            strings_positions[(line_number, file_position)] = line
        file.write('--------- The File End ----------')
    return strings_positions


# Выполнение
# ------ На вход функции "custom_write()"
my_file = 'module_7_2.txt'
my_string = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
# ------ Работа функции "custom_write()"
# Пишем в файл и получаем "Словарь на выход"
returned_dict = custom_write(my_file, my_string)
# ------ С выхода функции "custom_write()"
print('------ С выхода функции "custom_write()"')
pprint(returned_dict)
print('--------- The End ----------')

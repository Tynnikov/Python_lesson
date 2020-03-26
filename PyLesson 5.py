'''
Режим доступа к файлу:
r - Открыть файл на чтение (режим по умолчанию)
w - Открыть на запись. При этом удалить содержимое файла. Если файл не существует, создать новый.
x - Открыть файл на запись, если он не существует. Если файл существует, он не будет создан.
a - Открыть файл на дозапись. Добавить информацию в конец файла.
b - Открыть файл в двоичном формате.
t - Открыть файл в текстовом формате (режим по умолчанию)
+ - Открыть файл на чтение и запись

'''

# Задание - 1 Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

# with open('my_file.txt', 'w', encoding='utf-8') as f:
#     for line in range(3):
#         content = input('Word: ')  + ' \n'
#         f.write(content)
#
# with open('my_file.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)


# Задание - 2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке
# count = 0
# with open('new_file.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line_split = line.split(' ')
#         for i in range(len(line_split)):
#             count += 1
#     print(f'Количество слов в файле - {count}')

# Задание - 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 55 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# with open('salary.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line_split = line.split('-')
#         if int(line_split[1]) > 55000:
#             print(line)

# Задание - 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#
# def make_list():
#     with open('my_number.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             line_split = line.split('-')
#             num.append(line_split[1])
#
# def make_dict(key, value):
#     return dict(zip(key, value))
#
# def write_new_file(dct):
#     with open('new_number.txt', 'w', encoding='utf-8') as f:
#         for key, value in dct.items():
#             string = key + ' - ' + str(value) + ' \n'
#             f.write(string)
#
# words = ['Один', 'Два', 'Три', 'Четыре']
# num = []
#
# make_list()
# new_dict = make_dict(words, num)
# write_new_file(new_dict)

# Задание - 5 Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint


def make_list_random_number(start, end, count):
    return [randint(start, end) for i in range(count)]

def make_file(lst):
    with open('my_list_num.txt', 'w', encoding='utf-8') as f:
        for i in lst:
            string = str(i) + ' '
            f.write(string)

def get_sum_in_file():

    with open('my_list_num.txt', 'r', encoding='utf-8') as f:
        s = 0
        for line in f:
            line_split = line.split(' ')
            for i in range(len(line_split) - 1):
                s += int(line_split[i])
            print('Sum', s)


lst = make_list_random_number(-100, 100, 9)
make_file(lst)
get_sum_in_file()
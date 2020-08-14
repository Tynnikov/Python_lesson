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

with open('my_file.txt', 'w', encoding='utf-8') as f:
    for line in range(3):
        content = input('Word: ')  + ' \n'
        f.write(content)

with open('my_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')



# Задание - 2 Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

words = 0
lines = 0

with open('test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines += 1
        line_split = line.split(' ')
        for i in range(len(line_split)):
            words += 1
    print(f'Count words - {words}')
    print(f'Count lines - {lines}')

# Задание - 3 Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 55 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('salary.txt', 'r', encoding='utf-8') as file:
    list_salary = []
    for line in file:
        line_split = line.split(' ')
        list_salary.append(float(line_split[1]))
        number = float(line_split[1])
        if number < 55000:
            print(f'Salary: surname {line_split[0]} - {line_split[1]}')
    avg_of_salary = sum(list_salary) / len(list_salary)
    print(round(avg_of_salary, 2))

# Задание - 4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def make_list():
    with open('my_number.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line_split = line.split('-')
            num.append(line_split[1])

def make_dict(key, value):
    return dict(zip(key, value))

def write_new_file(dct):
    with open('new_number.txt', 'w', encoding='utf-8') as f:
        for key, value in dct.items():
            string = key + ' - ' + str(value) + ' \n'
            f.write(string)

words = ['Один', 'Два', 'Три', 'Четыре']
num = []

make_list()
new_dict = make_dict(words, num)
write_new_file(new_dict)

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

'''
Задание - 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

'''


with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in line)
        convert_str_to_int = [int(i) for i in new_str.split()]
        print(f'{line.split()[0]} {sum(convert_str_to_int)}')

'''
Задание - 7
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные 
о фирме: название, форма собственности, выручка, издержки. 

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json
result = []

with open('profit.json', 'w', encoding='utf-8') as write_file:
    with open('text.txt', 'r', encoding='utf-8') as read_file:
        profit = {}
        for line in read_file:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({'average_profit':round(average_profit)})
    json.dump(result, write_file)


# Задача-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# my_str = 'string'
# my_int = 7
# my_float = 3.14
# my_complex = (5, 6)
# my_list = [1, "hello", "world", None]
# my_tuple = (1, "hello", "world")
# my_dict = {'name': "Anton", 'age': 21}
# my_set = {1,2,2,2,2,2,3,3,4,5,5,6}
# my_bool = True
# my_bytesOrBytearray = bytes('text', encoding='utf-8')
# my_noneType = None
# #my_exceptions = 500/0 # исключения
#
# my_types = [my_str, my_int, my_float, my_complex, my_list, my_tuple, my_dict, my_set, my_bool, my_bytesOrBytearray,
#             my_noneType]
#
# for elem in my_types:
#     print(f'{elem}, - Элемент относится к типу -  {type(elem)}')


# Задание-2: Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# count = int(input('Введите количество раз, которое нужно ввести в список - '))
# i = 0
# my_list = []
# while i < count:
#     elements = input('Введите значение для списка - ')
#     my_list.append(elements)
#     i += 1
#
# if len(my_list) % 2 == 0:
#     i = 0
#     while i < len(my_list):
#         elem = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = elem
#         i += 2
# else:
#     i = 0
#     while i < len(my_list):
#         elem = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = elem
#         i += 2
#
# print(my_list)


# Задача-3: Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# num = int(input('Введите месяц в виде целого числа от 1 до 12 - '))
# months = {1: 'Январь',
#          2: 'Февраль',
#          3: 'Март',
#          4: 'Апрель',
#          5: 'Мая',
#          6: 'Июнь',
#          7: 'Июль',
#          8: 'Август',
#          9: 'Сентябрь',
#          10: 'Октябрь',
#          11: 'Ноябрь',
#          12: 'Декабрь'}
#
# if num == 1 or num == 2 or num == 12:
#     print(f'{months.get(num)} - это Зима')
# elif num == 3 or num == 4 or num == 5:
#     print(f'{months.get(num)} - это Весна')
# elif num == 6 or num == 7 or num == 8:
#     print(f'{months.get(num)} - это Лето')
# elif num == 9 or num == 10 or num == 11:
#     print(f'{months.get(num)} - это Осень')
# else:
#     print('Вы ввели некорректное значение')

# Задача-4: Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове

words = input('Введите предложение. Слова больше 10 букв будут сокращены. ')
list_of_words = words.split()
for idx, elem in enumerate(list_of_words):
    if len(elem) > 10:
        print(idx, elem[:10])
    else:
        print(idx, elem)

# Задача-5: Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

number = int(input('Введите число: '))
my_list = [7, 5, 3, 3, 2]
count_of_match = my_list.count(number)
del_last_elem = len(my_list)

for i in my_list:
    if count_of_match > 0:
        if number == i:
            match = my_list.index(i) + count_of_match
            my_list.insert(match, number)
            my_list.pop(del_last_elem)
            break

    elif count_of_match == 0:
        if number > i:
            match = my_list.index(i)
            my_list.insert(match, number)
            my_list.pop(del_last_elem - 1)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
            my_list.pop(del_last_elem - 1)
            break

print(my_list)


# box = ['apple', 'melon', 'banana', 'apple', 'melon', 'banana', 'apple', 'melon', 'banana','apple', 'melon', 'banana']
# lenght = len(max(box, key=len))
#
# for number, item in enumerate(box, start=1):
#     print('{}. {}'.format(number, item.rjust(lenght)))

# Задача - 6: *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {"название”: "компьютер”, "цена”: 20000, "количество”: 5, "eд”: "шт.”}),
#     (2, {"название”: "принтер”, "цена”: 6000, "количество”: 2, "eд”: "шт.”}),
#     (3, {"название”: "сканер”, "цена”: 2000, "количество”: 7, "eд”: "шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     "название”: ["компьютер”, "принтер”, "сканер”],
#     "цена”: [20000, 6000, 2000],
#     "количество”: [5, 2, 7],
#     "ед”: ["шт.”]
# }
# name_of_key = [el for el in input('напишет характеристики: ').split(" ")]  # поменять на input

# goods = [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."})
# ]

number = int(input("Какое количество товара будете заполнять: "))
goods = list()
my_dict = dict()

for i in range(1, number + 1):
    line = (i, {"название": input('Введите название: '), "цена": int(input('Введите цену: ')),
                "количество":  int(input('Введите количество: ')), "ед": input('Введите единицу измерения: ')})
    goods.append(line)

ask = 1
while ask == 1:
    my_list = list()
    name_of_key = input("Имя ключа: ")
    for i in goods:
        add_to_list = i[1].get(name_of_key)
        my_list.append(add_to_list)

    print(my_dict.setdefault(name_of_key, my_list))
    ask = int(input("Введите 1 - продолжить или любое число, чтобы выйти: "))

print("Аналитика о товарах:\n", my_dict)


# Дополнительное задание:
    
NAME = ['Ivan Ivanov', 'Petr Petrov', 'Alexandr SIdorov']
SALARY = [50000, 600000, 150000]


def convert_two_lists_to_dict(lst1, lst2):
    # вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
    return dict(zip(lst1, lst2))


def write_dict_to_salary_txt(dct):
    # Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
    # столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
    with open('salary.txt', 'w', encoding='utf-8') as f:
        for key, value in dct.items():
            string = key + ' - ' + str(value) + ' \n'
            f.write(string)


def read_file_minus_13_percent(file_name):
    # После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
    # Есть условие, не отображать людей получающих более зарплату 500000
    # Так же при выводе имя должно быть полностью в верхнем регистре!
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line_split = line.split(' - ')
            salary_value = int(line_split[1])   # перевел значения в числовой формат
            name = line_split[0]
            salary_tax = salary_value - (salary_value * 0.13)   # з/п за вычетом налогов
            if salary_tax <= 500000:    # - вариант включает в себя фильтр з/п с налогами
                print(name.upper(), salary_tax)
            #if salary_value <= 500000:  -  - вариант включает в себя фильтр з/п до налогов
            #    print(name, salary_tax)

print(convert_two_lists_to_dict(NAME, SALARY))
my_dict = convert_two_lists_to_dict(NAME, SALARY)
write_dict_to_salary_txt(my_dict)
read_file_minus_13_percent('salary.txt')

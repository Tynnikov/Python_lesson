# # Задание-1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
#

def division():
    print('Деление двух чисел')
    try:
        num_one = int(input('Введите число: '))
        num_two = int(input('Введите число: '))
        return num_one / num_two
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('Расчет невозможен. Введите число')
    return


print(division())

s1 = input('Enter the number: ')
s2 = input('Enter the number: ')

def del_number(s1, s2):
    try:
        print(int(s1/s2))
    except ZeroDivisionError:
        print('You can not divide by zero!')
    except TypeError:
        print('Use only numbers!')

del_number(s1, s2)


# Задание-2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def users(**kwargs):
    print(kwargs)

users(name='Petr', surname='Petrov', year='1990', city='Yekaterinburg', email='empty@mail.ru', number='+733390')


# Задание-3:
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_two_big_numbers(*args):
    summ = 0
    min_number = min(args)
    for i in args:
        summ += i
    print(summ - min_number)

n1 = int(input('Enter the number: '))
n2 = int(input('Enter the number: '))
n3 = int(input('Enter the number: '))
sum_two_big_numbers(n1, n2, n3)

# Задание-4:
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень

def my_func(x, y):
    return x ** abs(y)

print(my_func(2, -2))

def my_func(x, y):
    return x ** y

print(my_func(2, -3))

def my_func_1(x, y):
    for i in range(1, y):
        x += x
    return x

print(my_func_1(2, 3))


# Задание-5:
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_sum():
    summ = 0
    out = True
    while out == True:
        my_list_of_numbers = input('Enter the numbers with space. Add "q" to exit: ').split()


        for i in range(len(my_list_of_numbers)):
            if my_list_of_numbers[i] == 'q':
                print("Sum of all numbers: ", end='')
                out = False
            else:
                summ += int(my_list_of_numbers[i])
        print(summ)

my_sum()

# Задание-6:
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
#
def int_func(word):
    print(word.title())


def check_string(string):
    for i in string:
        if 97 <= ord(i) <= 122 or ord(i) == 32:
            continue
        else:
            print('Enter latin letters! Try again... ')
            break
    else:
        int_func(string)

s = input('Enter your words. Use lowcase and latin: ')

check_string(s)



#
#Extra ex:


# age = [10, 20, 30]
# name = ['misha', 'valera', 'oleg', 'empty']
#
# print(list(zip(age, name)))
# print(dict(zip(name, age)))
#
# for i, j in zip(age, name):
#     print(i, j)
#
#

#
# data = [1, 2, 3, 4, 5]
#
#
# # def my_pow(x):
# #     return x ** 2
# #
# #
# # print(list(map(my_pow, data)))
#
# result = list(map(lambda x: x ** 2, data))
# print(result, '- lambda')
 
#
# with open('9.txt' 'r') as file:
#     for line in file:
#         print()
#
# print()


#
#
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

# # Задание-1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
#

# def division():
#     print('Деление двух чисел')
#     try:
#         num_one = int(input('Введите число: '))
#         num_two = int(input('Введите число: '))
#         return num_one / num_two
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#     except ValueError:
#         print('Расчет невозможен. Введите число')
#     return
#
#
# print(division())

# Задание-2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# def users(**kwargs):
#     print(kwargs)
#
# users(name='Petr', surname='Petrov', year='1990', city='Yekaterinburg', email='empty@mail.ru', number='+733390')


# Задание-3:
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# def my_fanc(*args):
#     return args
#
# print(max(my_fanc(1, 22, -3)))

# Задание-4:
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень

def my_func(x, y):
    return x ** abs(y)

print(my_func(2, -2))
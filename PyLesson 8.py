''' Задание - 1:
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
class Data:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def convert_to_int_date(cls, date):
        str_date = date
        my_date = []
        for i in date.split():
            if i != '/':
                my_date.append(i)
        return cls(str_date)


    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31 and 1 <= int(month) <= 12 and 2019 >= year >= 0:
            print(f'Date: {day} {month} {year}')

d = '21/08/20'

data = Data(d)
print(data.convert_to_int_date(d))
print(type(data.str_date))
print(Data.valid_date(11, 12, 2020))


''' Задание - 2:
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
'''

class OwnError(Exception):
    pass


inp_data_1 = int(input("Введите положительное число: "))
inp_data_2 = int(input("Введите положительное число: "))

try:
    division = inp_data_1 / inp_data_2
    if inp_data_2 == 0:
        raise OwnError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
    inp_data = input('Введите число отличное от нуля: ')
else:
    print(f"Все хорошо. Ваше число: {inp_data_2}")


    
''' Задание - 3:
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять 
список только числами. Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит 
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами 
выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем 
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
'''
class Error(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())

''' Задание - 1:
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
''' Задание - 1:
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Date:
  def __init__(self, date_string):
    self.date_string = date_string

  @staticmethod
  def is_valid_date(date_string):
      day, month, year = parse_date_str(date_string)
      return is_day_valid(day) and is_month_valid(month) and is_year_valid(year)


def parse_date_str(date_string):
    day, month, year = date_string.split('-')
    return int(day), int(month), int(year)

def is_day_valid(day):
  if 1 <= day <= 31:
    return True
  return False

def is_month_valid(month):
  if 1 <= month <= 12:
    return True
  return False
  
def is_year_valid(year):
  if 0 < year:
    return True
  return False





assert parse_date_str('1-2-3') == (1,2,3)

assert is_day_valid(10)
assert not is_day_valid(132)
assert not is_day_valid(-1)
assert is_day_valid(1)
assert is_day_valid(31)

assert is_month_valid(12)
assert not is_month_valid(14)

assert not is_year_valid(-2020)
assert is_year_valid(20)
assert not is_year_valid(0)


date1 = Date('01-01-2000')
assert date1.date_string == '01-01-2000'


assert Date.is_valid_date('01-01-2020')
assert not Date.is_valid_date('123-01-2020')
assert not Date.is_valid_date('01-023-2020')
assert not Date.is_valid_date('01-02-0')

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

#.

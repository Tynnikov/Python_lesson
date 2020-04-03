''' Задание - 1:
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.  
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):

        count = 0
        while count < 5:
            for el in TrafficLight.__color:
                print(el)
                count += 1
                time.sleep(2)


# traffic = TrafficLight()
# traffic.running()

'''Задание - 2:
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''


class Road:
    weight = None
    thickness = None

    def __init__(self, weight, thickness):
        self._width = 20
        self._length = 50
        self.weight = weight
        self.thickness = thickness

    def wight_asphalt(self):
        return self.weight * self.thickness * self._width * self._length


# calc = Road(25,5)
# total = calc.wight_asphalt()
# print(f'Масса асфальта {total} тонн')

'''Задание - 3:
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return print(f'ФИО сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        return print(self._income.get('wage') + self._income.get('bonus'))


# emp = Position('Ivan', 'Ivanov', 'CEO', 100, 15)
# emp.get_full_name()
# emp.get_total_income()

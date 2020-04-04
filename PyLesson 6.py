''' Задание - 1:
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.  
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
# import time
#
#
# class TrafficLight:
#     __color = ['red', 'yellow', 'green']
#
#     def running(self):
#
#         count = 0
#         while count < 5:
#             for el in TrafficLight.__color:
#                 print(el)
#                 count += 1
#                 time.sleep(2)


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

#
# class Road:
#     weight = None
#     thickness = None
#
#     def __init__(self, weight, thickness):
#         self._width = 20
#         self._length = 50
#         self.weight = weight
#         self.thickness = thickness
#
#     def wight_asphalt(self):
#         return self.weight * self.thickness * self._width * self._length


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

#
# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return print(f'ФИО сотрудника {self.name} {self.surname}')
#
#     def get_total_income(self):
#         return print(self._income.get('wage') + self._income.get('bonus'))


# emp = Position('Ivan', 'Ivanov', 'CEO', 100, 15)
# emp.get_full_name()
# emp.get_total_income()

'''Задание - 4:
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
'''


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')

    def go(self):
        print(f'GO {self.name}')

    def stop(self):
        print(f'Stop {self.name}')

    def turn(self, direction):
        print(f'Direction {direction}')


class TownCar(Car):

    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def get_speed(self):
        return print(self.speed)

    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость {self.speed}. Скорость легкового автомобиля превышена')


class SportCar(Car):
    def __init__(self, name, speed, color, has_turbo=True):
        super().__init__(name, speed, color)
        self.has_turbo = has_turbo


class WorkCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def show_speed(self):
        if self.speed > 40:
            print(f'Ваша скорость {self.speed}. Скорость грузового автомобиля превышена')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True


town_car = TownCar('Lada', 61, 'red')
sport_car = SportCar('GTR', 300, 'red')
work_car = WorkCar('Kamaz', 45, 'yellow')
police_car = PoliceCar('Police', 65, 'black')

print('имя ', town_car.name)
print('цвет ', town_car.color)
print('скорость ', town_car.speed)
town_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('right')
town_car.show_speed()


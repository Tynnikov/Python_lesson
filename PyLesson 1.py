# 1) Поработайте с переменными, создайте несколько, выведите на экран,
#  запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# print("Hello")
# name = input("What is your name? ")
# age = int(input("How old you? "))
# print("My name is ", name, "I am - ", age)


# 2) Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# timeInSecond = int(input("Введите время в секундах: "))
# hour = timeInSecond // 3600
# minute = (timeInSecond % 3600) // 60
# second = minute // 60
# print(f"Текущее время {hour}:{minute}:{second}")

# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# number = input("Введите число: ")
# sumNumbers = int(number) + int(str(number+number)) + int(str(number+number+number))
# print(sumNumbers)

# 4)Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# number = input("Введите число: ")
#
# bigNumber = 0
# for i in number:
#     while bigNumber < int(i):
#         bigNumber = int(i)
#
# print(bigNumber)

# 5) Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# proceed = int(input("Введите выручку: "))
# costs = int(input("Введите ваши издержки: "))
#
# if proceed > costs:
#     profitability = proceed // costs
#     print(type(profitability))
#     print(f"Ваша прибыль больше расходов в {profitability} раз")
# else:
#     print("Ваши издержки превышают прибыль")
#
# employees = input("Сообщите количество сотрудников? ")
# profitForOneEmployee = profitability / int(employees)
# print(" Прибыль на одного сотрудника ", profitForOneEmployee)

# 6) Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.

DistanceFirstDay = int(input("Введите расстояние пройденное в первый день? "))
DistanceLastDay = int(input("Введите расстояние пройденное за все время? "))

countDays = 1
while DistanceLastDay > DistanceFirstDay:
    DistanceFirstDay += DistanceFirstDay / 10
    countDays += 1

print(f"Общий результат превышен, через {countDays}")
 
     









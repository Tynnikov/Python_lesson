''' Задание - 1:
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.


Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.

'''
# Вариант 1

# class Matrix():
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.matrix)
#
#     def __add__(self, other):
#         try:
#             m = [[int(self.matrix[line][itm]) + int(other.matrix[line][itm]) for itm in range(len(self.matrix[line]))]
#                  for line in range(len(self.matrix))]
#             return Matrix(m)
#         except IndexError:
#             return f'Ошибка размерности матрицы'

# Вариант 2
class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        l = []
        for i in range(len(self.matrix)):
            l.append([])
            for j in range(len(self.matrix[0])):
                l[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, l))

matrix_one = Matrix([[1, 2],
                     [3, 4],
                     [5, 6]])
matrix_two = Matrix([[10, 12],
                     [13,14],
                     [15,16]])

matrix_sum = matrix_one + matrix_two
print(matrix_one)
print(matrix_two)
print(matrix_sum)

'''
Задание - 2:
Реализовать проект расчета суммарного расхода ткани на 
производство одежды. Основная сущность (класс) этого 
проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) 
и рост (для костюма). Это могут быть обычные числа: V и H, 
соответственно. 
Для определения расхода ткани по каждому типу одежды использовать 
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на 
практике полученные на этом уроке знания: реализовать абстрактные 
классы для основных классов проекта, проверить на практике 
работу декоратора @property.
'''
class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())


'''
Задание - 3 :
Реализовать программу работы с органическими клетками, 
состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий 
количеству ячеек клетки (целое число). В классе должны быть 
реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), вычитание (__sub__()), 
умножение (__mul__()), деление (__truediv__()). 
Данные методы должны применяться только к клеткам и 
выполнять увеличение, уменьшение, умножение и обычное 
(не целочисленное) деление клеток, соответственно. 
В методе деления должно осуществляться округление значения 
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек 
общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять 
только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей 
клетки определяется как произведение количества ячеек этих 
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей 
клетки определяется как целочисленное деление количества ячеек 
этих двух клеток.
В классе необходимо реализовать метод make_order(), 
принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., 
где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний 
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество 
ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество 
ячеек в ряду — 5. Тогда метод make_order() вернет строку: 
*****\n*****\n*****.
'''

class Ceil():
    def __init__(self, nums):
        self.nums = nums

    def make_order_one(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def make_order_two(self, rows):
        row = ''
        for i in range(int(self.nums / rows)):
            row += f'{"*" * rows} \n'
        row += f'{"*" * (self.nums % rows)}'
        return row

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сумма ячейк: {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Вычитание невозможно'

    def __mul__(self, other):
        return f'Умножение ячейк: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'Деление ячейк: {self.nums // other.nums}'

ceil_one = Ceil(2000)
ceil_two = Ceil(100)
print(ceil_one + ceil_two)
# print(ceil_one - ceil_two)
# print(ceil_one * ceil_two)
# print(ceil_one // ceil_two)
print(ceil_two.make_order_one(21))
print(ceil_two.make_order_two(5))











# Extra
import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption('Kogalym King')

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'),
             pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'),
             pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'),
            pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'),
            pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()
music = pygame.mixer.music.load('Game/music.mp3')
pygame.mixer.music.play(-1)  # обеспечивает зацикливание музыки

score = 0


class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 28, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60)  # рисует hitbox вокруг персонажа
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy():
    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'),
                 pygame.image.load('Game/R3E.png'),
                 pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'),
                 pygame.image.load('Game/R6E.png'),
                 pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'),
                 pygame.image.load('Game/R9E.png'),
                 pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'),
                pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'),
                pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'),
                pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            # шкала здоровья
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            # отрисовка уменьшения здоровья
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')


def redrawGameWindow():
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) прямоугольник вместо героя
    win.blit(bg, (0, 0))  # создание фона
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = Player(200, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)  # fps
    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            man.hit()
            score -= 5

    if shootLoop > 0:  # исправление глюка с очередью из пуль
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        # Проверка координат по оси х и оси у
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))  # удаление пуль за границу

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))  # удаление пуль за границу

    keys = pygame.key.get_pressed()
    # vel - проверка, чтобы не было выхода за экран
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

            shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = - 1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg  # neg - имитация создания прыжка по "параболе"
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()

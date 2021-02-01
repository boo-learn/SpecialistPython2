# Напишите класс трапеции, свойства класса:
# координаты 4-х точек.
# Предусмотреть в классе конструктор и методы:
# проверка, является ли фигура равнобочной трапецией;
# вывод длин всех сторон,
# расчет периметра,
# расчет площадь.
#
# Создайте несколько объектов(трапеций) и проверьте созданный вами функционал.
# Считайте, что по заданным точкам можно построить трапецию. Проверять это не нужно!

import math

# представляет точку на плоскости
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# представляет трапецию
class Trapezoid:
    # инициализирует новый экземпляр класса Trapezoid
    def __init__(self, name, lbp, lup, rup, rbp):
        self.name = name    # условное название трапеции
        self.lbp = lbp      # left bottom point
        self.lup = lup      # left up point
        self.rup = rup      # right up point
        self.rbp = rbp      # right bottom point
        # вычилить расстояние между левыми точками трапеции
        self.left = self.distance(self.lbp, self.lup)
        # вычилить расстояние между правыми точками трапеции
        self.right = self.distance(self.rbp, self.rup)
        # вычилить расстояние между верхними точками трапеции
        self.up = self.distance(self.rup, self.lup)
        # вычилить расстояние между нижними точками трапеции
        self.bottom = self.distance(self.rbp, self.lbp)

    # возвращает строку - описание трапеции при использовании в функции print
    def __repr__(self):
        return self.info()

    # возвращает рассояние между двумя заданными точками
    def distance(self, point_1, point_2):
        return math.sqrt(math.pow(point_2.x - point_1.x, 2) + math.pow(point_2.y - point_1.y, 2))

    # возвращает значение "равнобочная", если левая и правая стороны равны; или неравнобочная - в ином случае
    def is_isosceles(self):
        # вернуть результат
        return f"{'равнобочная' if self.left == self.right else 'неравнобочная'}"

    # возвращает периметр трапеции
    def get_perimeter(self):
        # вернуть периметр трапеции как сумму всех сторон
        return self.left + self.up + self.right + self.bottom

    # возвращает площадь трапеции
    def get_area(self):
        # вычислить высоту трапеции
        h = math.fabs(self.lup.y - self.lbp.y)
        # вернуть площадь как произведение полусуммы оснований на высоту
        return ((self.up + self.bottom) / 2) * h

    # возвращает параметры трапеции в одной строке
    def info(self):
        return f"Трапеция {self.name}: {self.is_isosceles()}, периметр: {self.get_perimeter()}, площадь: {self.get_area()}"

# ========================================================================================
# ===================================== ПРОВЕРКИ =========================================
# ========================================================================================

# создать равнобочную трапецию
t1 = Trapezoid("Т1", Point(0,0), Point(2,5), Point(4,5), Point(6,0))
print(t1)

# создать неравнобочную трапецию
t2 = Trapezoid("Т2", Point(0,0), Point(3,5), Point(4,5), Point(6,0))
print(t2)

# создать прямоугольник (вырожденная трапеция - равнобочная)
t3 = Trapezoid("Т3", Point(0,0), Point(0,5), Point(6,5), Point(6,0))
print(t3)

# создать ещё одну неравнобочную трапецию
t4 = Trapezoid("Т4", Point(0,0), Point(0,5), Point(6,5), Point(12,0))
print(t4)

# Напишите класс трапеции, свойства класса:
# координаты 4-х точек.
# Предусмотреть в классе конструктор и методы:
# проверка, является ли фигура равнобочной трапецией;
# вывод длин всех сторон,
# расчет периметра,
# расчет площадь.
#
# Создайте несколько объектов(трапеций) и проверьте созданный вами функционал.

import math

class Trapezoid:
    # Трапеция ABCD
    # Большее основание (нижнее)- AD
    # Меньшее основание (верхнее)- BC
    # Основания - горизонтальны, т.е.
    # координаты y точек A и D - равны,
    # координаты y точек B и C - равны,
    # Начало координат необходимо выбрать так,
    # чтобы координаты всех точек были положительными
    #
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def height(self):
        # Высота трапеции
        return self.by - self.ay

    def length_ad(self):
        # Длина большего основания AD
        return self.dx - self.ax

    def length_bc(self):
        # Длина меньшего основания BC
        return self.cx - self.bx

    def length_ab(self):
        # Длина левой боковой стороны AB
        if self.ax == self.bx:
            return self.by - self.ay
        else:
            cat1 = self.height()
            cat2 = abs(self.bx - self.ax)
            return math.hypot(cat1, cat2)

    def length_cd(self):
        # Длина правой боковой стороны AB
        if self.cx == self.dx:
            return self.cy - self.dy
        else:
            cat1 = self.height()
            cat2 = abs(self.dx - self.cx)
            return math.hypot(cat1, cat2)

    def is_equilateral(self):
        # Трапеция равнобокая?
        return self.bx - self.ax == self.dx - self.cx

    def perimeter(self):
        # Периметр
        return self.length_ab() + self.length_bc() + self.length_cd() + self.length_ad()

    def area(self):
        # Площадь трапеции
        return (self.length_ad() + self.length_bc()) / 2 * self.height()

trapezoid_1 = Trapezoid(0, 0, 3, 4, 5, 4, 8, 0)
print('Трапеция 1')
print(f'B ({trapezoid_1.bx}, {trapezoid_1.by}), C ({trapezoid_1.cx}, {trapezoid_1.cy})')
print(f'A ({trapezoid_1.ax}, {trapezoid_1.ay}), D ({trapezoid_1.dx}, {trapezoid_1.dy})')
print(f'    Высота трапеции = {trapezoid_1.height()}')
print(f'       Основание BC = {trapezoid_1.length_bc()}')
print(f'       Основание AD = {trapezoid_1.length_ad()}')
print(f' Боковая сторона AB = {trapezoid_1.length_ab()}')
print(f' Боковая сторона CD = {trapezoid_1.length_cd()}')
print(f'Равнобокая трапеция = {trapezoid_1.is_equilateral()}')
print(f'           Периметр = {trapezoid_1.perimeter()}')
print(f'            Площадь = {trapezoid_1.area()}')

trapezoid_2 = Trapezoid(1, 0, 1, 4, 4, 4, 7, 0)
print('Трапеция 2')
print(f'B ({trapezoid_2.bx}, {trapezoid_2.by}), C ({trapezoid_2.cx}, {trapezoid_2.cy})')
print(f'A ({trapezoid_2.ax}, {trapezoid_2.ay}), D ({trapezoid_2.dx}, {trapezoid_2.dy})')
print(f'    Высота трапеции = {trapezoid_2.height()}')
print(f'       Основание BC = {trapezoid_2.length_bc()}')
print(f'       Основание AD = {trapezoid_2.length_ad()}')
print(f' Боковая сторона AB = {trapezoid_2.length_ab()}')
print(f' Боковая сторона CD = {trapezoid_2.length_cd()}')
print(f'Равнобокая трапеция = {trapezoid_2.is_equilateral()}')
print(f'           Периметр = {trapezoid_2.perimeter()}')
print(f'            Площадь = {trapezoid_2.area()}')

trapezoid_3 = Trapezoid(1, 1, 4, 5, 7, 5, 7, 1)
print('Трапеция 3')
print(f'B ({trapezoid_3.bx}, {trapezoid_3.by}), C ({trapezoid_3.cx}, {trapezoid_3.cy})')
print(f'A ({trapezoid_3.ax}, {trapezoid_3.ay}), D ({trapezoid_3.dx}, {trapezoid_3.dy})')
print(f'    Высота трапеции = {trapezoid_3.height()}')
print(f'       Основание BC = {trapezoid_3.length_bc()}')
print(f'       Основание AD = {trapezoid_3.length_ad()}')
print(f' Боковая сторона AB = {trapezoid_3.length_ab()}')
print(f' Боковая сторона CD = {trapezoid_3.length_cd()}')
print(f'Равнобокая трапеция = {trapezoid_3.is_equilateral()}')
print(f'           Периметр = {trapezoid_3.perimeter()}')
print(f'            Площадь = {trapezoid_3.area()}')

trapezoid_4 = Trapezoid(2, 1, 1, 5, 4, 5, 7, 1)
print('Трапеция 4')
print(f'B ({trapezoid_4.bx}, {trapezoid_4.by}), C ({trapezoid_4.cx}, {trapezoid_4.cy})')
print(f'A ({trapezoid_4.ax}, {trapezoid_4.ay}), D ({trapezoid_4.dx}, {trapezoid_4.dy})')
print(f'    Высота трапеции = {trapezoid_4.height()}')
print(f'       Основание BC = {trapezoid_4.length_bc()}')
print(f'       Основание AD = {trapezoid_4.length_ad()}')
print(f' Боковая сторона AB = {trapezoid_4.length_ab()}')
print(f' Боковая сторона CD = {trapezoid_4.length_cd()}')
print(f'Равнобокая трапеция = {trapezoid_4.is_equilateral()}')
print(f'           Периметр = {trapezoid_4.perimeter()}')
print(f'            Площадь = {trapezoid_4.area()}')

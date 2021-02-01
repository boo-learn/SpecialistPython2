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

class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def len_edges(self):
        len_12 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        len_23 = ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** 0.5
        len_34 = ((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2) ** 0.5
        len_41 = ((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2) ** 0.5

        return [len_12, len_23, len_34, len_41]

    def perimetr(self):
        return sum(self.len_edges())

    def area(self):
        h = self.y2 - self.y1
        a = self.len_edges()[1]
        b = self.len_edges()[3]
        return 0.5 * h * (a + b)

    def is_equilateral(self):
        return f"Трапеция равнобочная" if self.len_edges()[0] == self.len_edges()[2] else f"Трапеция неравнобочная"


trapez = Trapezoid(0, 0, 2, 4, 6, 4, 8, 0)
print(trapez.len_edges())
print(f"Длина стороны 1_2: {trapez.len_edges()[0]}")
print(trapez.perimetr())
print(trapez.area())
print(trapez.is_equilateral())

trapez2 = Trapezoid(0, 0, 2, 4, 6, 4, 9, 0)
print(trapez2.len_edges())
print(f"Длина стороны 1_2: {trapez2.len_edges()[0]}")
print(trapez2.perimetr())
print(trapez2.area())
print(trapez2.is_equilateral())

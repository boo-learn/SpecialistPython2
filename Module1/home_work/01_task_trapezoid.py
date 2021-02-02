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


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        ans = Vector(self.x - other.x, self.y - other.y)
        return ans

    def __eq__(self, other):
        return True if (self.x == other.x) and (self.y == other.y) else False

    def __repr__(self):
        return f"vec| {self.x}, {self.y}"

    def is_parallel(self, other):
        return True if self.cross(other) == 0 else False

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def cross(self, other):
        cross = self.x * other.y - self.y * other.x
        return cross


class Edge:
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end

    pass


class Trapezoid:
    def __init__(self, vertices):
        """p_i --> радиус-векторы вершин
            В пределах конструктора мы будем находить первое попавшееся оснолвание трапеции
        """
        self.vertices = vertices
        self._starting_vert = 3;
        base_edge = self.vertices[self._starting_vert] - self.vertices[self._starting_vert - 1]
        true_starting = False
        for j in range(1, 4, 1):
            edge = self.vertices[self._starting_vert - j] - self.vertices[self._starting_vert - j - 1]
            if edge.is_parallel(base_edge):
                true_starting = True
                break
        if not true_starting:
            self._starting_vert = 2;

    def __repr__(self):
        s = "Trapezoid| "
        for i in range(len(self.vertices)):
            s += f"p{i}: {self.vertices[i].x},{self.vertices[i].y} "

        return s

    # проверка, является ли фигура равнобочной трапецией;
    def is_isosceles(self):
        edge1 = self.vertices[self._starting_vert - 1] - self.vertices[self._starting_vert - 2]
        edge2 = self.vertices[self._starting_vert - 3] - self.vertices[self._starting_vert - 4]
        return edge2.length() == edge1.length()

    # вывод длин всех сторон,
    def list_of_sidelengths(self):
        for j in range(4):
            edge = self.vertices[self._starting_vert - j] - self.vertices[self._starting_vert - j - 1]
            print(edge.length())

    # расчет периметра,
    def perimeter(self):
        p = 0
        for j in range(4):
            edge = self.vertices[self._starting_vert - j] - self.vertices[self._starting_vert - j - 1]
            p += edge.length()
        return p

    # расчет площадь.
    def area(self):
        d1 = self.vertices[self._starting_vert - 0] - self.vertices[self._starting_vert - 2]
        d2 = self.vertices[self._starting_vert - 1] - self.vertices[self._starting_vert - 3]
        area = abs(0.5 * d1.cross(d2))
        return area


try:
    p1 = Vector(1, 1)
    p2 = Vector(3, 1)
    p3 = Vector(4, 0)
    p4 = Vector(0, 0)
    verts = [p1, p2, p3, p4]
    tr1 = Trapezoid(verts)
    print(tr1)
    # print(tr1._starting_vert)
    print(tr1.is_isosceles())
    print(tr1.perimeter())
    print(tr1.area())

    p1 = Vector(1, 1)
    p2 = Vector(3, 1)
    p3 = Vector(1, -1)
    p4 = Vector(0, 0)
    verts = [p1, p2, p3, p4]
    tr2 = Trapezoid(verts)
    print(tr2)
    print(tr2.is_isosceles())

    p1 = Vector(1, 1)
    p2 = Vector(0, 1)
    p3 = Vector(0, 0)
    p4 = Vector(1, 0)
    verts = [p1, p2, p3, p4]
    tr3 = Trapezoid(verts)
    print(tr3)
    print(tr3.is_isosceles())
    print(tr3.perimeter())
    print(tr3.area())
except Exception as e:
    print(e)

    pass

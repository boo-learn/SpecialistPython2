# Задание "Векторы"

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self

    def __sub__(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __isub__(self, other_vector):
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self

    def __mul__(self, scalar:int):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar:int):
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 5)
v2 = Vector(4, 7)
print(f"сумма:        {v1} + {v2} = {v1 + v2}")
print(f"разность:     {v1} - {v2} = {v1 - v2}")
print(f"произведение: {v1} * 3 = {v1 * 3} (= {3 * v1})")

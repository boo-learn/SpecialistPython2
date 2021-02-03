class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        res_x = self.x + vector.x
        res_y = self.y + vector.y
        res_vector = Vector(res_x, res_y)
        return res_vector

    def __sub__(self, vector):
        res_x = self.x - vector.x
        res_y = self.y - vector.y
        res_vector = Vector(res_x, res_y)
        return res_vector

    def __mul__(self, scalar):
        res_x = self.x * scalar
        res_y = self.y * scalar
        res_vector = Vector(res_x, res_y)
        return res_vector

    def __rmul__(self, scalar):
        res_x = self.x * scalar
        res_y = self.y * scalar
        res_vector = Vector(res_x, res_y)
        return res_vector

    def __repr__(self):
        return f'({self.x}, {self.y})'

v1 = Vector(1,2)
v2 = Vector(1,2)
v3 = v1 + v2
v4 = v1 - v2
scalar = 6
v5 = v1 * scalar
print(f" v1: {v1}")
print(f" v2: {v2}")
print(f" v3 = v1 + v2: {v3}")
print(f" v4 = v1 - v2: {v4}")
print(f" v5 = v1 * {scalar}: {v5}")

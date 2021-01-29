class Vector(list):

    def __init__(self,x,y):
        list.__init__(self,[x,y])

    def __sub__(self, invect):
        templst = [vi - wi for vi, wi in zip(self, invect)]
        return Vector(templst[0],templst[1])

    def __mul__(self, k):
        templst = [vi * k for vi in self]
        return Vector(templst[0],templst[1])

    def __add__(self,invect):
        templst = [v + w for v, w in zip(self, invect)]
        return Vector(templst[0],templst[1])

    def as_point(self):
        return self[0], self[1]

    # def __str__(self):
         # return "V(x:{} y:{})".format(self[0], self[1])


v1 = Vector(31,44)
v2 = Vector(42,53)

print('Сложение векторов:')

v3 = v1 + v2
print(f'V{v1} + V{v2} = V{v3}')

print('Вычитание векторов: ')

v4 = v3 - v1
print(f'V{v3} - V{v1} = V{v4}')

print('Умножение вектора на скаляр(число): ')

k = -3
v5 = v1 * k

print(f'V{v5} = V{v1} * {k}')

k = 3
v6 = v1 * k

print(f'V{v6} = V{v1} * {k}')

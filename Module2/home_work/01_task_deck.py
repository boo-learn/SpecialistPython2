class Vector:
    # Вектор a.
    # Принимаемые параметры - координаты конца вектора x, y.
    # Пример: v = Vector(4, 3)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # Форматируем вывод функцией print()
        return f'Вектор ({self.x}, {self.y})'

    def __add__(self, b):  # Сложение векторов
        return Vector(self.x + b.x, self.y + b.y)

    def __sub__(self, b):  # Вычитание векторов
        return Vector(self.x - b.x, self.y - b.y)

    def __mul__(self, k):
        # Умножение вектора на скаляр b = a * k
        # При k > 0 получим сонаправленный вектор
        # При k < 0 получим противоположно направленный вектор
        return Vector(self.x * k, self.y * k)


a = Vector(4, 5)
print(f'a = {a}')

b = Vector(2, 3)
print(f'b = {b}')

print(f'a + b = {a + b}')
print(f'a - b = {a - b}')

print(f'a * 3 = {a * 3}')
print(f'a * (-3) = {a * (-3)}')

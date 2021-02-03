# Сюда отправляем решение задачи "Вектор"Vector.py
Без общего доступа
Тип
Текст
Размер
1 КБ (1 228 байт)
Использовано
1 КБ (1 228 байт)
Расположение
python_study
Владелец
я
Изменено
мной 2 февр. 2021 г.
Открыто
мной 2 февр. 2021 г.
Создано
2 февр. 2021 г. в приложении Google Drive Web
Добавить описание
Читателям разрешено скачивать файл
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        ans = Vector(self.x - other.x, self.y - other.y)
        return ans

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        pass

    def __eq__(self, other):
        return True if (self.x == other.x) and (self.y == other.y) else False

    def __matmul__(self, scalar_factor):
        return self.scale(scalar_factor)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def is_parallel(self, other):
        return True if self.cross(other) == 0 else False

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def cross(self, other):
        cross = self.x * other.y - self.y * other.x
        return cross

    def scale(self, factor):
        return Vector(self.x * factor, self.y * factor)


if __name__ == "__main__":
    v1 = Vector(1, 1)
    v2 = Vector(2, 3)
    v3 = Vector(2, 2)

    print(f"{v1} + {v2} = {v1 + v2}")
    print(f"{v2} + {v3} = {v2 + v3}")
    print(f"2 * {v1}  = {2 * v1}")
    print(f"{v1 * 2}")
    print(f"{v1} @ 2 - {v3}  = {v1 @ 2 - v3}")

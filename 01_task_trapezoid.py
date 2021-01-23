import math
class Trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1  # Координаты точки A
        self.y1 = y1  # Координаты точки A
        self.x2 = x2  # Координаты точки B
        self.y2 = y2  # Координаты точки B
        self.x3 = x3  # Координаты точки C
        self.y3 = y3  # Координаты точки C
        self.x4 = x4  # Координаты точки D
        self.y4 = y4  # Координаты точки D

    # проверка на равнобедрие
    def isosceles(self, x1, y1, x2, y2, x3, y3, x4, y4):
        print("Проверка на равнобедрие трапеции:")
        BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        AD = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        if AD == BC:
            print("Трапеция - равнобедренная!")
        else:
            print("Трапеция - не равнобедренная!")

    def get_length(self, x1, y1, x2, y2, x3, y3, x4, y4):
        print("Находим длины сторон трапеции:")
        AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        CD = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        AD = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        return f"Длины сторон трапеции равны: AB = {AB}, BC = {BC}, CD = {CD}, AD = {AD}"

    def get_perimeter(self, x1, y1, x2, y2, x3, y3, x4, y4):
        print("Вычисляем периметр трапеции:")
        AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        CD = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        AD = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        p = AB + BC + CD + AD
        return f"Периметр трапеции равен: {p}"

    def get_area(self, x1, y1, x2, y2, x3, y3, x4, y4):
        print("Вычисляем площадь трапеции:")
        h = abs(y2 - y3)
        AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        CD = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        s = h * (AB + CD) / 2
        return f"Площадь трапеции равна: {s}"

    def checking_on_trapeze(self, y1, y2, y3, y4):
        print("Проверяем является ли четырехугольник трапецией:")
        if ((y1 == y2) & (y3 == y4)):
            flag = True
            print("ABCD - трапеция!")
            print("AB и CD - основания трапеции!")
            print("AD и BC - боковые стороны трапеции!")
        else:
            flag = False
            print("ABCD - не трапеция!")


trapeze1 = Trapeze(3,7,9,7,12,3,1,3)

trapeze1.checking_on_trapeze(7,7,3,3)
print(trapeze1.get_length(3,7,9,7,12,3,1,3) + "\n")

trapeze1.checking_on_trapeze(7,7,3,3)
trapeze1.isosceles(3,7,9,7,12,3,1,3)
print()

trapeze1.checking_on_trapeze(7,7,3,3)
print(trapeze1.get_perimeter(3,7,9,7,12,3,1,3) + "\n")

trapeze1.checking_on_trapeze(7,7,3,3)
print(trapeze1.get_area(3,7,9,7,12,3,1,3))

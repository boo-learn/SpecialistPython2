import math


class Dot:  # Точка с координатами x,y
    def __init__(self, x, y):
        self.x = x
        self.y = y


def length(dotM, dotN):
    length_MN = math.sqrt((dotM.x - dotN.x) ** 2 + (dotM.y - dotN.y) ** 2)
    return length_MN


class Trapecia:  # Трапеция задана точками А,В,С,D с левой нижней вершины по час. стрелке
    def __init__(self, dotA, dotB, dotC, dotD):
        self.dotA = dotA
        self.dotB = dotB
        self.dotC = dotC
        self.dotD = dotD

    def dliny(self):  # Длины сторон
        st_AB = length(self.dotA, self.dotB)
        st_BC = length(self.dotC, self.dotB)
        st_CD = length(self.dotC, self.dotD)
        st_AD = length(self.dotA, self.dotD)
        storony = []
        storony.append(st_AB)
        storony.append(st_BC)
        storony.append(st_CD)
        storony.append(st_AD)
        return storony

    def vyvod(self):  # Вывод сторон
        print(
            f'AB={(self.dliny())[0]:.3},  BC={(self.dliny())[1]:.3},  CD={(self.dliny())[2]:.3},  AD={(self.dliny())[3]:.3}')
        return

    def proverka(self):  # Проверка на равносторонность
        if (self.dliny())[0] == (self.dliny())[2]:
            print('Трапеция равносторонняя')
        else:
            print('Трапеция неравносторонняя')
        return

    def perimetr(self):  # Периметр
        p = 0
        for stor in self.dliny():
            p += stor
        print(f'Периметр = {p:.3}')
        return

    def ploshad(self):  # Площадь
        a = (self.dliny())[1]  # сторона АС
        b = (self.dliny())[3]  # сторона AD
        c = (self.dliny())[0]  # сторона АВ
        d = (self.dliny())[2]  # сторона CD
        m = (a + b) / 2  # сред линия
        h = math.sqrt(c ** 2 - (((b - a) ** 2 + c ** 2 - d ** 2) / (2 * (b - a))) ** 2)  # высота
        s = m * h  # площадь
        print(f'Площадь = {s:.3}')
        return


print('ТРАПЕЦИЯ 1')
dot1 = Dot(1, 1)
dot2 = Dot(2, 4)
dot3 = Dot(5, 4)
dot4 = Dot(8, 1)
trapec1 = Trapecia(dot1, dot2, dot3, dot4)
trapec1.dliny()
trapec1.vyvod()
trapec1.proverka()
trapec1.perimetr()
trapec1.ploshad()
print()

print('ТРАПЕЦИЯ 2')
dot1 = Dot(1, 1)
dot2 = Dot(2, 4)
dot3 = Dot(5, 4)
dot4 = Dot(6, 1)
trapec2 = Trapecia(dot1, dot2, dot3, dot4)
trapec2.dliny()
trapec2.vyvod()
trapec2.proverka()
trapec2.perimetr()
trapec2.ploshad()

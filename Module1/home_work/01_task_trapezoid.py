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
    def __init__(self,t_x1,t_y1,t_x2,t_y2,t_x3,t_y3,t_x4,t_y4):
        self.t_x1 = t_x1
        self.t_y1 = t_y1
        self.t_x2 = t_x2
        self.t_y2 = t_y2
        self.t_x3 = t_x3
        self.t_y3 = t_y3
        self.t_x4 = t_x4
        self.t_y4 = t_y4

    @staticmethod
    def sidelength(x1,y1,x2,y2):
            return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

    def perimeter(self):
            return self.sidelength(self.t_x1,self.t_y1,self.t_x2,self.t_y2) + self.sidelength(self.t_x2,self.t_y2,self.t_x3,self.t_y3) + self.sidelength(self.t_x3,self.t_y3,self.t_x4,self.t_y4) + self.sidelength(self.t_x4,self.t_y4,self.t_x1,self.t_y1)

    def showsidelength(self):
            print("Длины сторон: ")
            print("AB = " + str(self.sidelength(self.t_x1,self.t_y1,self.t_x2,self.t_y2)))
            print("BC = " + str(self.sidelength(self.t_x2,self.t_y2,self.t_x3,self.t_y3)))
            print("CD = " + str(self.sidelength(self.t_x3,self.t_y3,self.t_x4,self.t_y4)))
            print("DA = " + str(self.sidelength(self.t_x4,self.t_y4,self.t_x1,self.t_y1)))

    def sq_trap(self):
            c = self.sidelength(self.t_x2,self.t_y2,self.t_x3,self.t_y3)
            a = self.sidelength(self.t_x1,self.t_y1,self.t_x2,self.t_y2)
            b = self.sidelength(self.t_x3,self.t_y3,self.t_x4,self.t_y4)
            h = math.sqrt(c**2 - ((a - b ) / 2)**2) 
            s = ((a + b )/ 2) * h
            return s
            
    def check_trap(self):
        if(self.sidelength(self.t_x1,self.t_y1,self.t_x3,self.t_y3) == self.sidelength(self.t_x2,self.t_y2,self.t_x4,self.t_y4)):
            return True
        else:
            return False


trap1 = Trapezoid(1,1, 5,1, 4,4, 2,4)

print("Трапеция 1");

if(trap1.check_trap()):
    print("Периметр P = " +str(trap1.perimeter()))
    trap1.showsidelength()
    print("Площадь S = " +str(trap1.sq_trap()))
else:
    print("Это не трапеция !!!")
    
trap2 = Trapezoid(1,1, 5,1, 5,4, 2,4)

print("Трапеция 2");

if(trap2.check_trap()):
    print("Периметр P = " +str(trap2.perimeter()))
    trap2.showsidelength()
else:
    print("Это не равнобедренная трапеция !!!")

# Напишите класс трапеции, свойства класса:
# координаты 4-х точек.
# Предусмотреть в классе конструктор и методы:
# проверка, является ли фигура равнобочной трапецией;
# вывод длин всех сторон,
# расчет периметра,
# расчет площадь.
#
# Создайте несколько объектов(трапеций) и проверьте созданный вами функционал.
import math as m


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
        # side c: (x1,y1) (x2,y2) 
        self.__c = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # side b: (x2,y2) (x3,y3) base of the trapezoid  
        self.__b = m.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        # side d: (x3,y3) (x4,y4) 
        self.__d = m.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        # side a: (x4,y4) (x1,y1) base of the trapezoid 
        self.__a = m.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        
    def is_isosceles(self):
        if self.__c == self.__d: 
            return True
        else:
            return False
        
    def show_sides(self):
        return f'c = {self.__c}, b = {self.__b}, d = {self.__d}, a = {self.__a}'
        
    def perimeter(self):
        return self.__a + self.__b + self.__c + self.__d
    
    def area(self):
        # semi-perimeter
        s_p = self.perimeter() / 2
        # 1st part of the formula
        form_1part = (self.__a + self.__b) / abs(self.__a - self.__b) 
        # 2nd part of the formula
        form_2part = m.sqrt((s_p - self.__a) * (s_p - self.__b)
                            * (s_p - self.__a - self.__c)
                            * (s_p - self.__a - self.__d))
        return form_1part * form_2part
    
        
def main():
    tr1 = Trapezoid(0, 0, 1, 2, 4, 2, 4, 0)
    print('-' * 10)
    print('1st trapezoid')
    print(f'Sides: {tr1.show_sides()}')
    print(f'Is it isosceles? {tr1.is_isosceles()}')
    print(f'Perimeter: {tr1.perimeter()}')
    print(f'Area: {tr1.area()}')
    
    tr2 = Trapezoid(0, 0, 1, 2, 4, 2, 5, 0)
    print('-' * 10)
    print('2nd trapezoid')
    print(f'Sides: {tr2.show_sides()}')
    print(f'Is it isosceles? {tr2.is_isosceles()}')
    print(f'Perimeter: {tr2.perimeter()}')
    print(f'Area: {tr2.area()}')
    
    
if __name__=='__main__':
    main()
    

    

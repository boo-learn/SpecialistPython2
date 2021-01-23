# # Напишите класс трапеции, свойства класса:
# # координаты 4-х точек.
# # Предусмотреть в классе конструктор и методы:
# # проверка, является ли фигура равнобочной трапецией;
# # вывод длин всех сторон,
# # расчет периметра,
# # расчет площадь.
# #
# # Создайте несколько объектов(трапеций) и проверьте созданный вами функционал.
#
crd1=[1,1]
crd2=[2,3]
crd3=[3,3]
crd4=[4,1]

class Trapezoid:
    def __init__(self,coords1,coords2,coords3,coords4):
           self.c1=[coords1,coords2,coords3,coords4]
           #self.c2=coords2
           #self.c3=coords3
           #self.c4=coords4

    # определяем уравнения прямых, функция подходит для любого многоугольника
    # для определения угла наклона к оси Х и определения паралельных
    def lines(self):
        line=[]
        from math import inf
        for i in range (-1,len(self.c1)-1):
            if (self.c1[i][0]-self.c1[i+1][0])==0:
                line.append(inf)
            else:
                line.append((self.c1[i][1]-self.c1[i+1][1])/(self.c1[i][0]-self.c1[i+1][0]))
        return line
    # проверяем, является ли набор координат трапецией
    def if_trapezoid(self):
        l1= self.lines()
        return ((l1[0]==l1[2])and(l1[1]!=l1[3]))or((l1[0]!=l1[2])and(l1[1]==l1[3]))
    # вычисляем длины сторон, функция подходит для любого замкнутого многоугольника
    def t_lens(self):
        lens=[]
        c1=self.c1
        from math import sqrt
        for i in range (-1,len(self.c1)-1):
            lens.append(sqrt((c1[i+1][1]-c1[i][1])**2+(c1[i+1][0]-c1[i][0])**2))
        return lens
    # вычисляем периметр
    def perimetr(self):
        return sum(self.t_lens())
    # вычисляем площадь по сложной формуле, функция подходит для любого замкнутого многоугольника
    def sq(self):
        c1=self.c1
        from math import fabs
        sum1=(c1[-1][0]*c1[0][1]-c1[0][0]*c1[-1][1])
        for i in range (0,len(self.c1)-1):
            sum1+=c1[i][0]*c1[i+1][1]-c1[i+1][0]*c1[i][1]
        return fabs(sum1)/2
    def ravnobok(self):
        l1=self.t_lens()
        return (l1[0]==l1[3])or(l1[1]==l1[3])

trapez1=Trapezoid(crd1,crd2,crd3,crd4) #равнобокая трапеция
trapez2=Trapezoid([1,2],[2,4],[5,3],[3,-1]) #кривая трапеция
trapez3=Trapezoid([2,1],[0,5],[5,5],[3,1]) # равнобокая трапеция
trapez4=Trapezoid([0,0],[-3,5],[0,5],[3,5]) # паралелограмм вообще-то, но прочие функции работают
trapez5=Trapezoid([0,0],[0,5],[5,5],[5,0]) # квадрат вообще-то, но прочие функции работают
trapez6=Trapezoid([1,0],[0,2],[3,4],[5,0]) #еще одна кривая трапеция

print(trapez1.if_trapezoid())
print (trapez1.sq())
print(trapez1.ravnobok())
print('---'*10)
print(trapez2.lines())
print(trapez2.if_trapezoid())
print(trapez2.perimetr())
print(trapez2.sq())
print(trapez2.t_lens())
print(trapez2.ravnobok())
print('---'*10)
print(trapez3.if_trapezoid())
print (trapez3.sq())
print(trapez3.ravnobok())
print('---'*10)
#print(trapez2.if_trapezoid())
print('---'*10)
print(trapez4.if_trapezoid())
print('---'*10)
print(trapez5.if_trapezoid())
print(trapez5.lines())
print(trapez5.perimetr())
print(trapez5.sq())
print(trapez5.ravnobok())
print('---'*10)
print(trapez6.lines())
print(trapez6.if_trapezoid())
print('периметр=',trapez6.perimetr())
print(trapez6.sq())
print(trapez6.t_lens())
print(trapez6.ravnobok())

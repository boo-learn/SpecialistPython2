class Vector: # для любой размерности векторов

    def __init__ (self, coords):
        self.coords=list(coords) # координаты преобразуются в список для работы
        self.l=len(coords) # вычисляется размерность системы координат


    def normalise (self,other): # нормализация добавляются необходимое количество координат, для нормальной работы
        if self.l>other.l:
            while len(other.coords)!=len(self.coords):
                other.coords.append(0)
        else:
            while len(self.coords) != len(other.coords):
                self.coords.append(0)


    def __add__(self, other): # сложение векторов подходит для любой размерности
        if self.l!=other.l:
            self.normalise(other)
        summa=[]
        for i in range (0,self.l):
            summa.append(self.coords[i]+other.coords[i])
        return Vector (summa)

    def __sub__(self, other): #  вычитание векторов подходит для любой размерности
        if self.l !=other.l:
            self.normalise(other)
        summa=[]
        for i in range (0,self.l):
            summa.append(self.coords[i]-other.coords[i])
        return Vector (summa)

    def __mul__(self, other): # умножение векторов на число (скаляр) подходит для любой размерности
        summa=[]
        for i in range (0,self.l):
            summa.append(self.coords[i]*other)
        return Vector (summa)

    def __pow__(self, other): # перемножение векторов
        if self.l!=other.l:
            self.normalise(other)
        summa = []
        for i in range(0, self.l):
            summa.append(self.coords[i] * other.coords[i])
        return Vector(summa)

    def mod (self): # модуль, длина вектора
        from math import sqrt
        summa = 0
        for i in range(0, self.l):
            summa+=(self.coords[i] * self.coords[i])
        return sqrt(summa)

    def tol (self): # преобразование вектора в список для печати
        return list(self.coords)

    def __xor__(self, other): # угол между двумя векторами, возвращает угол в градусах для интереса
        from math import sqrt
        from math import acos
        from math import pi
        if self.l!=other.l:
            self.normalise(other)
        sum1=0
        sum2=0
        sum3=0
        for i in range(0, self.l):
            sum1 += (self.coords[i] * other.coords[i])
            sum2 += self.coords[i]*self.coords[i]
            sum3 += other.coords[i]*other.coords[i]
        if sum2*sum3==0:
            return 0
        else:
            return acos(sum1/sqrt(sum2)/sqrt(sum3))/pi*180







v1=Vector((-1,1,1,3))
v2=Vector((2,2,2,2))
v21=Vector((2,-1))
v22=Vector((-1,3))

v11=Vector((1,0,1))
v12=Vector((0,1,0))
v3=v1+v2

#v1.normalise(v11)
#print (v1.tol())
#print (v11.tol())

print(f"  сложение 1 {v1.tol()} и 2 {v2.tol()} ==    {(v1+v2).tol()} ")
print(f"  сложение 21 {v21.tol()} и 22 {v22.tol()} ==    {(v21+v22).tol()} ")
print(f"  вычитание 21 {v21.tol()} и 22 {v22.tol()} ==     {(v22-v21).tol()} ")
print(f"  вычитание 1 {v1.tol()} - 2 {v2.tol()} ==     {(v2-v1).tol()}")
print(f" умножение 2 {v2.tol()} на число 4  {(v2*4).tol()}")
print(f" скалярное произведение векторов 1 {v1.tol()} и 2 {v2.tol()} {(v2**v1).tol()}")
print(f" модуль вектора  2 {v2.tol()} (длина)  { v2.mod() }")
print(f" модуль вектора  3 {v3.tol()} (длина)  { v3.mod() }")
print(f" угол между векторами 2 {v2.tol()} и 3 {v3.tol()} == { v2^v3 } градусов")
print(f" угол между векторами 11 {v11.tol()} и 12 {v12.tol()}  == { v11^v12 } градусов")
print(f" угол угла между векторами 21 {v21.tol()} и 22 {v22.tol()} ==    {(v21^v22) } градусов ")
print(f" угол между векторами 1 {v1.tol()} и 22 {v22.tol()} с нормализацией    {(v1^v22) } градусов ")
print(f" новые координаты 1 {v1.tol()} и 22 {v22.tol()} ")
print(type(v1))
print(type(v3))

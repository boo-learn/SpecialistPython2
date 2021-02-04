# Сюда отправляем решение задачи "Вектор"
class Vector:  # Вектор с координатами x,y
    def __init__(self, m):
        self.x = m[0]
        self.y = m[1]

    def __repr__(self):
        return f'({self.x}; {self.y})'

    # def summa(self,vect):
    #     rez_x=self.x+vect.x
    #     rez_y = self.y + vect.y
    #     return f'({rez_x}; {rez_y})'

    def __add__(self, vect):
        rez_x = self.x + vect.x
        rez_y = self.y + vect.y
        return f'({rez_x}; {rez_y})'

    def __sub__(self, vect):
        rez_x = self.x - vect.x
        rez_y = self.y - vect.y
        return f'({rez_x}; {rez_y})'

    # def multipl(self,scalar):
    #     rez_x = self.x*scalar
    #     rez_y = self.y*scalar
    #     return f'({rez_x}; {rez_y})'

    def __mul__(self,scalar):
        rez_x = self.x*scalar
        rez_y = self.y*scalar
        return f'({rez_x}; {rez_y})'






vect1=Vector((-1,1))
print('Вектор 1:',vect1)

vect2=Vector((5,-2))
print('Вектор 2:',vect2)

print(f'vect1+vect2 = {vect1+vect2}')
print(f'vect1-vect2 = {vect1-vect2}')

print(f'vect1*6 = {vect1*6}')


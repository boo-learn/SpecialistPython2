class Fraction:
    def __init__(self, fract_str:str): # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        pair=fract_str.split()
        if len(fract_str.split(' ')) == 1:
            f=fract_str.split('/')
            self.numerator = int(f[0])
            self.denominator = int(f[1])
        else:
            whole=pair[0]
            f=pair[1].split('/')
            self.numerator = int(f[0]) # числителя
            self.denominator = int(f[1]) # знаменателя
            self.numerator += abs(int(whole)) * self.denominator
            if int(whole) < 0:
                self.numerator *= -1
        # # целую часть перебрасываем в знаменатель
        # минус, если он есть, тоже храним в знаменателе

    def __add__(self, other:str):
        pair=other.split('/')
        if len(pair) == 2:
            if self.denominator == Fraction(other).denominator:
                self.numerator += Fraction(other).numerator
                return f'{self.denominator}/{self.numerator}'
            else:
                h=self.denominator * Fraction(other).denominator
                temp1=h/self.denominator
                temp2=h/Fraction(other).denominator
                return f'{temp1*self.numerator+temp2*Fraction(other).numerator}/{h}'
        else:
            print(other)
            return f'{int(self.denominator)*int(other)+self.numerator}/{self.denominator}'

    def __sub__(self, other):
        if self.denominator == Fraction(other).denominator:
            self.numerator -= Fraction(other).numerator
            return f'{self.denominator}/{self.numerator}'
        else:
            h=self.denominator * Fraction(other).denominator
            temp1=h/self.denominator
            temp2=h/Fraction(other).denominator
            return f'{temp1*self.numerator-temp2*Fraction(other).numerator}/{h}'

    def __mul__(self, other):
        return f'{self.numerator*Fraction(other).numerator}/{self.denominator*Fraction(other).denominator}'

    def __lt__(self, other):
        if self.denominator == Fraction(other).denominator:
            return self.numerator < Fraction(other).numerator
        else:
            h = self.denominator * Fraction(other).denominator
            temp1 = h / self.denominator
            temp2 = h / Fraction(other).denominator
            return f'{temp1*self.numerator<temp2*Fraction(other).numerator}'

    def __gt__(self, other):
        if self.denominator == Fraction(other).denominator:
            return self.numerator > Fraction(other).numerator
        else:
            h = self.denominator * Fraction(other).denominator
            temp1 = h / self.denominator
            temp2 = h / Fraction(other).denominator
            return f'{temp1*self.numerator>temp2*Fraction(other).numerator}'

# Примеры создания дробей:
fract1 = Fraction("3 12/15")
print(fract1.numerator,'/',fract1.denominator)
fract2 = Fraction("-1 2/6")
fract3 = Fraction("2/4")
fract4 = Fraction("-2/4")

print(fract3+'2/3')
print(fract3-'2/3')
print(fract3*'2/3')
print(fract3<'2/3')
print(fract3+'3')

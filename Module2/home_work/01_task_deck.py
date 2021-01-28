class Fraction:
    def __init__(self, string):
        integer = 0
        if '/' not in string:
            self.numerator = int(string)
            self.denominator = 1
            return
        if ' ' in string:
            integer = string.split(' ')[0]
            if integer:
                integer = int(integer)
                self.numerator = int(string.split(' ')[1].split('/')[0])
                self.denominator = int(string.split(' ')[1].split('/')[1])
        else:
            self.numerator = int(string.split('/')[0])
            self.denominator = int(string.split('/')[1])

        minus = False
        if integer < 0:
            minus = True
        self.numerator += abs(integer)*self.denominator
        if minus:
            self.numerator *= -1

    # 5 4/11
    # 55/11 + 4/11
    # def __init__(self, str):
    #     pattern = r'(-?\d*)\s?(\d*)/?(\d*)'
    #     res  = re.match(pattern, str)
    #     print(res.groups())
    #     result =
    #     if len(res.groups()) == 3:
    #         self.numerator = int(res.groups()[1]) + abs(int(res.groups()[0])) * int(res.groups()[2])
    #         self.denominator = int(res.groups()[2])
    #     elif len(res.groups()) == 2:
    #         self.numerator = int(res.groups()[0])
    #         self.denominator = int(res.groups()[2])
    #     else:
    #         self.numerator = int(res.groups()[0])
    #         self.denominator = 1

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if self.denominator == other.denominator:
            common_den = self.denominator
        else:
            common_den = self.denominator * other.denominator
        numerator1 = self.numerator * (common_den//self.denominator)
        numerator2 = other.numerator * (common_den//other.denominator)
        drob= Fraction.sokr(numerator1 + numerator2,common_den)
        return Fraction(f"{drob[0]}/{drob[1]}")

    @staticmethod # сокращает дробь до наименьшего числителя и знаменателя
    def sokr(num,denom):
        sig=1
        if num<0:
            sig=-1
            num=abs(num)
        num1 = num
        while num1>1:
            if denom%num1==0 and num%num1==0:
                num=num//num1
                denom=denom//num1
                num1=num
                #print (f"num {num} denom {denom} num1 {num1 } ") отладка
            else:
                num1-=1
                #print(f"num1 >>> {num1}") отладка
        return (num*sig,denom)


    def to_prn (self): # распечатка дробей с выделением целой части, так правильнее
        s=1
        if self.numerator<0:
           s=-1
        if abs(self.numerator)//self.denominator == 0:
            return (f"{self.numerator}/{self.denominator}")
        else:
            integer=s*(abs(self.numerator)//self.denominator)
            return (f"{integer} {abs(self.numerator)%self.denominator}/{self.denominator}")


    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        drob=Fraction.sokr(self.numerator * other.numerator,self.denominator * other.denominator)
        return Fraction(f"{drob[0]}/{drob[1]}")

    def __div__ (self, other): # не понятно, почему данная функция не перезагружается ????
        drob = Fraction.sokr(self.numerator * other.denominator,self.denominator * other.numerator)
        return Fraction(f"{drob[0]}/{drob[1]}")

# 4/5 + 7/12 = 4*12/60 + 7*5/60 48 + 35  = 83/60
# 4/5 + 5/1 = 4/5 + 25/5
f1 = Fraction("4/5")
f2 = Fraction("7/15")
f3 = Fraction("-5/2")
f4 = Fraction("-5")
f11=Fraction('7 1/12')
f12=Fraction('1 15/17')
f0 = Fraction("1")

print(f0.to_prn())
print(f" {f12.to_prn()} * {f0.to_prn()} ={(f12*f0).to_prn()}")
a=Fraction("-2444/104408")
print(a)
print(f" a=   {a.to_prn()}")

print(f"{a.to_prn()} сокращение {(a*f0).to_prn()}")

f5 = f1 + f2
print(f5)
print(f5.to_prn())
print('>>>')
print(f" {f11.to_prn()} * {f12.to_prn()} ={(f11*f12).to_prn()}")

print(f" {f11.to_prn()} / {f12.to_prn()} ={(f11.__div__(f12)).to_prn()}")

print(f" {f3.to_prn()} * {f4.to_prn()} = {(f3*f4).to_prn()}")



f6 = f1 + 5
# f1.__add__(5)
f7 = 5 + f1

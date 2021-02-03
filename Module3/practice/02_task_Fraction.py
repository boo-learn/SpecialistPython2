## Задание "Простые дроби"

# Сюда отправляем задание с классом дроби

class Fraction:
    def __init__(self, fract_str:str): # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        pair = fract_str.split()
        if len(pair) == 1:
            f = fract_str.split("/")
            self.numerator = int(f[0])
            self.denominator = int(f[1])
        else:
            whole = int(pair[0])
            f = pair[1].split("/")
            self.numerator = int(f[0])
            self.denominator = int(f[1])

            self.numerator += abs(whole) * self.denominator
            if whole < 0:
                self.numerator *= -1

    def __add__(self, fract_2):
        if self.denominator == fract_2.denominator:
            res_numerator = self.numerator + fract_2.numerator
            res_denominator = self.denominator
            return Fraction(f"{res_numerator}/{res_denominator}")

        res_denominator = self.denominator * fract_2.denominator
        res_numerator = self.numerator * fract_2.denominator + fract_2.numerator * self.denominator
        return Fraction(f"{res_numerator}/{res_denominator}")

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def sum_int(self,number):
        if type(self)==int and type(number)==string:
            (self,number)=(number,self)
        res_numerator=self.numerator+number*self.denominator
        res_denominator=self.denominator
        return Fraction(f"{res_numerator}/{res_denominator}")
        

# Примеры создания дробей:
fract1 = Fraction("5/6")
# print(fract1.numerator, "/", fract1.denominator)
fract2 = Fraction("-1/3")
print(fract1 + fract2)
# print(fract2.numerator, "/", fract2.denominator)
fract3 = Fraction("2/4")
fract4 = Fraction("-2/4")

print(fract1.sum_int(2))

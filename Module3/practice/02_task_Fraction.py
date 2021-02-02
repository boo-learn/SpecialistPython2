# Задание "Простые дроби"

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
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе

    def sum_fract(self,fract):
        self.numerator=self.numerator*fract.denominator+fract.numerator*self.denominator
        self.denominator*=fract.denominator
        print(self.numerator,"/",self.denominator)
        return

# Примеры создания дробей:
fract1 = Fraction("3 12/15")

fract2 = Fraction("-1 2/6")
fract3 = Fraction("2/4")
fract4 = Fraction("-2/4")


# Сложение дробей
fract1.sum_fract(fract2)

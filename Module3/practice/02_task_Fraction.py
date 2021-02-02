# Задание "Простые дроби"

# Сюда отправляем задание с классом дроби

class Fraction:
    def __init__(self, fract_str): # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде
        self.numerator = ... # числителя
        self.denominator = ... # знаменатель
        # целую часть перебрасываем в числитель
        # минус, если он есть, тоже храним в числителе
    def plus(self, fract_other):
        resultnum = self.numerator +  fract_other.numerator
        resulrdenom = self.denominator +  fract_other.denominator
        return f'{resultnum}/{resulrdenom}'    

# Примеры создания дробей:
fract1 = Fraction("3 12/15")
fract2 = Fraction("-1 2/6")
fract3 = Fraction("2/4")
fract4 = Fraction("-2/4")

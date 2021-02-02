class Fraction:
    def __init__(self, fract_str: str): # Дробь в конструктор передается в виде строки
        # А мы храним дробь в виде

        self.str = fract_str.strip()
        fract_to_list = self.str.split(' ')
        if len(fract_to_list) == 2:
            self.denominator = int(fract_to_list[1].split('/')[1])
            if int(fract_to_list[0]) >= 0:
                self.numerator = int(self.denominator) * int(fract_to_list[0]) + int(fract_to_list[1].split('/')[0])
            else:
                self.numerator = int(self.denominator) * int(fract_to_list[0]) - int(fract_to_list[1].split('/')[0])
        else:
            fract_to_list = fract_to_list[0].split('/')
            self.denominator = int(fract_to_list[1])
            self.numerator = int(fract_to_list[0])

        # self.numerator = ... # числителя
        # self.denominator = ... # знаменателя
        # целую часть перебрасываем в знаменатель
        # минус, если он есть, тоже храним в знаменателе
    def sum_fractions(self, fract_2):
        if self.denominator == fract_2.denominator:
            res_numerator = self.numerator + fract_2.numerator
            res_denominator = self.denominator
            res_fract = str(res_numerator) + '/' + str(res_denominator)
            res = Fraction(res_fract)
            return res
        else:
            res_denominator = self.denominator * fract_2.denominator
            res_numerator = self.numerator * fract_2.denominator + fract_2.numerator * self.denominator
            res_fract = str(res_numerator) + '/' + str(res_denominator)
            res = Fraction(res_fract)
            return res

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

# Примеры создания дробей:
fract1 = Fraction("2/15")
print(fract1.numerator)
print(fract1.denominator)
fract2 = Fraction("1/15")
print(fract2.numerator)
print(fract2.denominator)
print(fract1.sum_fractions(fract2))

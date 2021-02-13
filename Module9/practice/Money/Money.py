class Money:
    def __init__(self, rub, kop):
            self.rub = int(rub)
            self.kop = int(kop)

    def __add__(self, other):
            res = self.rub * 100 + self.kop
            other = other.rub * 100 + other.kop
            res = res + other
            return Money(res//100, res%100)

    def __sub__(self, other):
            res = self.rub * 100 + self.kop
            other = other.rub * 100 + other.kop
            res = res - other
            return Money(res//100, res%100)

    def __mul__(self, num):
            res = self.rub * 100 + self.kop
            res *= num
            return Money(res//100, res%100)

    def __lt__(self, other):
        res = self.rub * 100 + self.kop
        other = other.rub * 100 + other.kop
        return res < other

    def __eq__(self, other):
        res = self.rub * 100 + self.kop
        other = other.rub * 100 + other.kop
        return res == other

    def __ne__(self, other):
        res = self.rub * 100 + self.kop
        other = other.rub * 100 + other.kop
        return res != other

    def __gt__(self, other):
        res = self.rub * 100 + self.kop
        other = other.rub * 100 + other.kop
        return res > other

    def __repr__(self):
        if self.kop > 99:
            self.rub += self.kop//100
            self.kop = self.kop%100
        return str(self.rub) + 'руб ' + str(self.kop) + 'коп'

# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 321)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1) # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
#
# # Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп
print(money_sum1 > money_sum2)
print(money_sum1 == money_sum2)

class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop
        if kop > 99:
            self.rub += kop // 100
            self.kop = kop % 100

    def __add__(self, other):
        self_all = self.rub * 100 + self.kop
        other_all = other.rub * 100 + other.kop
        sum = self_all + other_all
        new_rub = sum // 100
        new_kop = sum % 100
        return Money(new_rub, new_kop)

    def __repr__(self):
        return f"{self.rub} руб. {self.kop} коп."

m1 = Money(1, 30)
m2 = Money(2,90)

print(f"{m1} + {m2} = {m1 + m2}")

m3 = Money(11, 88)
m4 = Money(7,57)

print(f"{m3} + {m4} = {m3 + m4}")

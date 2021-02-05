class Money:
    def __init__(self, rub, cop):
        self.rub = rub
        if cop // 100 > 0:
            rub += cop // 100
            cop = cop % 100
        self.cop = cop

    def __repr__(self):
        return f"{self.rub} руб. {self.cop} коп."

    def __add__(self, other):
        res_cop = self.cop + other.cop
        res_rub = self.rub + other.rub
        res_money = Money(res_rub, res_cop)
        return res_money

    def __sub__(self, other):
        money1 = self.rub*100 + self.cop
        money2 = other.rub*100 + other.cop
        res_money = money1 - money2

        if res_money >= 0:
            res = Money(0, res_money)
            return res
        else:
            raise ValueError("Некорректная сумма")

        res_cop = self.cop + other.cop
        res_rub = self.rub + other.rub
        res_money = Money(res_rub, res_cop)
        return res_money

m1 = Money(1, 20)
m2 = Money(1, 10)
m3 = m1+m2
print(m3)

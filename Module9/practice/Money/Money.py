class Money:
    def __init__(self, rub, kop_in):
        
        self.total_kop = rub * 100 + kop_in

    @property
    def rub(self):
        return self.total_kop // 100
    
    @property
    def kop(self):
        return self.total_kop % 100


    def __repr__(self):
        return f"{self.rub} р. {self.kop} к."
    
    
    def __add__(self, other_money):
        
        new_total_kop = self.total_kop + other_money.total_kop
        new_rub = new_total_kop // 100
        new_kop = new_total_kop % 100
        return Money(new_rub, new_kop)

    
    
money_sum1 = Money(20, 655)
print(money_sum1)
money_sum2 = Money(10, 45)
print(money_sum2)

money_sum3 = money_sum1 + money_sum2
print(money_sum3)








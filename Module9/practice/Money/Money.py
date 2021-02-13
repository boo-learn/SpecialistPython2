class Money:
    def __init__(self, rub, kop_in):
        if kop_in >= 100:
            self.rub = rub + kop_in // 100
            self.kop = kop_in % 100
        else:
            self.rub = rub
            self.kop = kop_in
    
    def __repr__(self):
        return f"{self.rub} р. {self.kop} к."
    
    
    def __add__(self, other_money):
        
        new_rub = self.rub + other_money.rub
        new_kop = self.kop + other_money.kop
        if new_kop >=100:
            new_rub = new_rub + new_kop // 100
            new_kop = new_kop % 100
         
        return Money(new_rub, new_kop)

    
    
money_sum1 = Money(20, 655)
print(money_sum1)
money_sum2 = Money(10, 45)
print(money_sum2)

money_sum3 = money_sum1 + money_sum2
print(money_sum3)







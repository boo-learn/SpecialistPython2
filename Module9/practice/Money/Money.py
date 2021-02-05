class Money:
    def __init__(self, rub,kop=0):
        self.rub = rub
        self.kop = kop

    def __repr__(self):
        return f'{self.rub+self.kop//100} руб. {self.kop%100} коп.'

    def __add__(self, money):
        rez_rub=self.rub+money.rub
        rez_kop = self.kop + money.kop
        return f'{rez_rub+rez_kop//100} руб. {rez_kop%100}'

    def procent(self, proc):
        rez_rub=((self.rub*100+self.kop)*proc/100)//100
        rez_kop = ((self.rub*100+self.kop)*proc/100)%100
        return f'{rez_rub+rez_kop//100} руб. {rez_kop%100}'

money1=Money(10,125)
print(money1)

money2=Money(10,12)
print(money2)

print(money1+money2)

print(money2.procent(10))

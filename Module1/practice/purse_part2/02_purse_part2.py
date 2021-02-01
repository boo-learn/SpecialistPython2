class Purse:
    def __init__(self,first_name,last_name,additional_name,sity,money):
        self.first_name = first_name
        self.last_name = last_name
        self.additional_name =  additional_name
        self.sity = sity
        self.__balance = 0
        self.currency = money
        self.history={
            'transfer': [],
            'income': [],
            'withdraw': []
        }
        self.status=None

    def income(self, summa):
        if self.status == 'open':
            self.__balance += summa
            self.save_history(f"Пополнено {summa}")
        elif self.status == 'block':
            raise ValueError('income',f"Кошелёк {self.first_name, self.last_name,self.additional_name} заблокирован")
    def transfer(self,summa,other_purse):
        if self.status == 'open':
            self.withdraw(summa)
            other_purse.income(summa)
            self.save_history('transfer',f"Переведено {summa}, на кошелек {other_purse.first_name, other_purse.last_name, other_purse.additional_name}")
        elif self.status == 'block':
            raise ValueError(f"Кошелёк {self.first_name, self.last_name,self.additional_name} заблокирован")
    def withdraw(self,summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        elif summa < 0:
            raise ValueError("Сумма должна быть положительной")
        elif self.status == 'open':
            self.__balance -= summa
            self.save_history('withdraw',f"Снято {summa}")
    def save_history(self,name_operation,operation):
        self.history[name_operation].append(operation)
    def info(self):
        print(f"Purse: owner:{self.first_name, self.last_name,self.additional_name} __balance: {self.__balance}, where you live: {self.sity}")
        print(self.history)
    def block_purse(self):
        self.status='block'
    def unblock_purse(self):
        self.status='open'
purse1= Purse('Ivan','Kapysta','Borisov','Mocsow','rub')
purse2= Purse('Vasya','Dodo','Antonov','Piter','rub')
try:
    purse1.info()
    purse2.info()
    purse1.income(300)
    purse2.income(400)
    purse1.info()
    purse1.transfer(100,purse2)
    purse1.info()
except ValueError as s:
    print(s)

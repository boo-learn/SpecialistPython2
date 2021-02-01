class User:
    def __init__(self,first_name,last_name, additional_name,city):
        self.first_name = first_name
        self.last_name = last_name
        self.additional_name = additional_name
        self.city=city

    def info(self):
        return f'{self.first_name} {self.last_name} {self.additional_name}'

class Operation:
    INCOME = 'income'
    WITHDRAW= 'withdraw'
    TRANSFER= 'transfer'
    def __init__(self,type,summa,target=None):
        self.type = type
        self.summa= summa
        self.target = target

    def info(self):
        return f"{self.type} summa: {self.summa} {f' to {self.target}' if self.target else ''}"

class Purse:
    OPEN = 'open'
    CLOSE = 'close'
    def __init__(self,first_name,last_name, additional_name,city,money):
        self._owner=User(first_name,last_name, additional_name,city)
        self.__balance = 0
        self._currency = money
        self._history=[]
        self._status=Purse.OPEN

    def income(self, summa):
        if self._status == Purse.OPEN:
            self.__balance += summa
            operation = Operation(Operation.INCOME, summa)
            self._history.append(operation)
        elif self._status == 'block':
            raise ValueError('income',f"Кошелёк {self._owner.info()} заблокирован")

    def transfer(self,summa,other_purse):
        if self._status == Purse.OPEN:
            self.withdraw(summa)
            other_purse.income(summa)
            operation = Operation(Operation.TRANSFER, summa,other_purse._owner.info())
            self._history.append(operation)
            # self.save_history('transfer',f"Переведено {summa}, на кошелек {other_purse.first_name, other_purse.last_name, other_purse.additional_name}")
        elif self.status == 'block':
            raise ValueError(f"Кошелёк {self._owner.info()} заблокирован")

    def withdraw(self,summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        elif summa < 0:
            raise ValueError("Сумма должна быть положительной")
        elif self._status == 'open':
            self.__balance -= summa
            operation = Operation(Operation.WITHDRAW, summa)
            self._history.append(operation)
            # self.save_history('withdraw',f"Снято {summa}")

    # def save_history(self,name_operation,operation):
    #     self.history[name_operation].append(operation)

    def info(self):
        return f'Purse| owner: {self._owner.info()} balance: {self.__balance} {self._currency}'

    def show_history(self, filter_type=None):
        filter_type=input("Введите операцию которую вы хотите посмотреть:\n1. income; \n2. withdraw\n3. transfer\n4. None\n")
        for hist in self._history:
            if filter_type == Operation.INCOME:
                if Operation.INCOME in hist.info():
                    print(hist.info())
            elif filter_type==Operation.WITHDRAW:
                if Operation.WITHDRAW in hist.info():
                    print(hist.info())
            else:
                print(hist.info())

    def block_purse(self):
        self.status='block'
    def unblock_purse(self):
        self.status='open'
purse1= Purse('Ivan','Kapysta','Borisov','Mocsow','rub')
purse2= Purse('Vasya','Dodo','Antonov','Piter','rub')
# purse1.unblock_purse()
purse1.income(200)
purse1.transfer(100,purse2)
purse2.income(300)
purse1.income(500)
purse2.income(600)
purse2.transfer(300,purse1)
purse2.transfer(200,purse1)
print(purse1.info())
print(purse1.show_history())
print(purse2.info())
print(purse2.show_history())
# try:
#     purse1.info()
#     purse2.info()
#     purse1.income(300)
#     purse2.income(400)
#     purse1.info()
#     purse1.transfer(100,purse2)
#     purse1.info()
# except ValueError as s:
#     print(s)

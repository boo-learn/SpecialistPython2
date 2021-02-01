class User:
    def __init__(self, name, surname, middle_name, city):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.city = city

    def info(self):
        return f"{self.surname} {self.name[0]}.{self.middle_name[0]}."


class Operation:
    INCOME = "income"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"

    def __init__(self, type, summa, target=None):
        self.type = type
        self.summa = summa
        self.target = target

    def info(self):
        return f"{self.type} sum:{self.summa}{f' to/from {self.target}' if self.target else ''}"


class Purse:
    def __init__(self, name, surname, middle_name, city, money):
        self.owner = User(name, surname, middle_name, city)
        self.__balance = 0
        self.currency = money
        self.history = []
        self.status = 'open'

    def income(self, summa, from_purse='None'):
        if self.status == 'open' and from_purse == 'None':
            self.__balance += summa
            operation = Operation(Operation.INCOME, summa)
            self.history.append(operation)
        elif self.status == 'open' and from_purse != 'None':
            self.__balance += summa
            operation = Operation(Operation.INCOME, summa, from_purse.info())
            self.history.append(operation)
        elif self.status == 'block':
            raise ValueError(f"Кошелёк {self.owner.info()} заблокирован")

    def transfer(self, summa, other_purse):
        if self.status == 'open':
            self.withdraw(summa, other_purse)
            other_purse.income(summa, other_purse)
            #self.save_history('transfer',f"Переведено {summa}, на кошелек {other_purse.owner.info()}")
            #self.history.append(Operation(Operation.TRANSFER, summa, other_purse.info()))
        elif self.status == 'block':
            raise ValueError(f"Кошелёк {self.owner.info()} заблокирован")

    def withdraw(self, summa, other_purse='None'):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        elif summa < 0:
            raise ValueError("Сумма должна быть положительной")
        elif self.status == 'open' and other_purse=='None':
            self.__balance -= summa
            #self.save_history('withdraw', f"Снято {summa}")
            self.history.append(Operation(Operation.WITHDRAW, summa))
        elif self.status == 'open' and other_purse!='None':
            self.__balance -= summa
            self.history.append(Operation(Operation.WITHDRAW, summa, other_purse.info()))
    # def save_history(self, name_operation, operation):
    #     self.history[name_operation].append(operation)

    def info(self):
        return f"P| owner:{self.owner.info()} balance: {self.__balance} {self.currency}"

    def show_history(self, filter_type=None):
        for hist in self.history:
            print(hist.info())

    def block_purse(self):
        self.status = 'block'

    def unblock_purse(self):
        self.status = 'open'


purse1 = Purse('Ivan', 'Kapysta', 'Borisov', 'Mocsow', 'rub')
purse2 = Purse('Vasya', 'Dodo', 'Antonov', 'Piter', 'rub')
purse1.unblock_purse()
purse2.unblock_purse()
purse1.income(200)
purse1.income(100)
purse1.income(500)
purse1.show_history()
purse2.show_history()
print('==============')
purse1.transfer(150, purse2)
purse1.show_history()
purse2.show_history()
# purse1.withdraw(100)
# purse1.transfer(100, purse2)

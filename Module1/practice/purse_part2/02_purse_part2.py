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
        return f"{self.type} sum:{self.summa}{f' to {self.target.owner.info()}' if self.target else ''}"

class Purse:
    BLOCK = 0
    OPEN = 1

    def __init__(self, name, surname, middle_name, city, money):
        self.owner = User(name, surname, middle_name, city)
        self.__balance = 0
        self.currency = money
        self.history = []
        self.status = Purse.OPEN

    def income(self, summa):
        if self.status == Purse.OPEN:
            self.__balance += summa
            operation = Operation(Operation.INCOME, summa)
            self.history.append(operation)
        elif self.status == Purse.BLOCK:
            raise ValueError(f"Кошелёк {self.owner.info()} заблокирован")

    def transfer(self, summa, other_purse):
        if self.status == Purse.OPEN:
            self.withdraw(summa)
            operation1 = Operation(Operation.TRANSFER, summa, other_purse)
            self.history.append(operation1)
            other_purse.income(summa)
            operation2 = Operation(Operation.INCOME, summa)
            other_purse.history.append(operation2)
        elif self.status == Purse.BLOCK:
            raise ValueError(f"Кошелёк {self.owner.info()} заблокирован")

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        if summa < 0:
            raise ValueError("Сумма должна быть положительной")

        self.__balance -= summa
        #self.save_history('withdraw', f"Снято {summa}")

    # def save_history(self, name_operation, operation):
    #     self.history[name_operation].append(operation)

    def info(self):
        return f"P| owner:{self.owner.info()} balance: {self.__balance} {self.currency}"

    def show_history(self, filter_type=None):
        for hist in self.history:
            print(hist.info())

    def block_purse(self):
        self.status = Purse.BLOCK

    def unblock_purse(self):
        self.status = Purse.OPEN


purse1 = Purse('Ivan', 'Kapysta', 'Borisov', 'Mocsow', 'rub')
purse2 = Purse('Vasya', 'Dodo', 'Antonov', 'Piter', 'rub')
purse1.unblock_purse()
purse2.unblock_purse()
purse1.income(200)
purse1.income(100)
purse1.income(500)
print(f"история кошелька {purse1.owner.info()}")
purse1.transfer(50, purse2)
purse1.show_history()
print(f"история кошелька {purse2.owner.info()}")
purse2.show_history()

#purse1.show_history()
# purse1.withdraw(100)
# purse1.transfer(100, purse2)

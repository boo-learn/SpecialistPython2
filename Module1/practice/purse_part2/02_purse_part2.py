class Purse:
    def __init__(self, name, patronymic, surname, city,  currency):
        self.owner_name = name
        self.patronymic = patronymic
        self.surname = surname
        self.city = city
        self.__balance = 0
        self.currency = currency
        self.history = []
        self.block = 0

    def income(self, summa):
        self.__balance += summa
        self.history.append({"income", summa})

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= summa
        self.history.append({"withdraw", summa})

    def transfer(self, other_purse, summa):
        self.withdraw(summa)
        other_purse.income(summa)
        self.history.append({"transfer", summa})

    def operations_history(self, key):
        if key == 0:
            print(self.history)

    def blocking(self, key = 0):
        if key == 0:
            self.block = 0
        else:
            self.block = 1

    def info(self):
        print(f"Purse| owner:{self.owner_name, self.surname} balance: {self.__balance} {self.currency}")

purse1 = Purse("Иван", "Петрович", "Сидоров", "Москва", "rub")
# purse2 = Purse("Вася", "rub")
purse1.income(200)
purse1.income(100)

print(purse1.history)
purse1.info()
# purse2.info()

# try:
#     purse1.transfer(purse2, 50)
# except ValueError as e:
#     print(e)

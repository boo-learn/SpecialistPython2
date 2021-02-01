class Purse:
    def __init__(self, firstname, middlename, lastname, city, currency): # конструктор
        self.owner_firstname = firstname
        self.owner_middlename = middlename
        self.owner_lastname = lastname
        self.city = city
        self.__balance = 0
        self.currency = currency
        self.history = list

    def income(self, summa):
        self.__balance += summa
        self.history.append(self, "пополнен на " + summa + " " + self.currency)

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= summa
        self.history.append(self, "снятие " + summa + " " + self.currency)

    def transfer(self, other_purse, summa):
        self.withdraw(summa)
        other_purse.income(summa)
        self.history.append(self, "перевод " + summa + " " + self.currency + " на кошелек " + other_purse.owner_lastname)

    def showhistory(self, actiontype):
        if(actiontype == 0):
            print(self.history)

    def info(self):
        # self - ссылка на объект, для которого был вызван данный метод
        print(f"Purse| owner:{self.owner_firstname} {self.owner_lastname} balance: {self.__balance} {self.currency}")



purse1 = Purse("Иван", "Петрович", "Петров", "Москва", "rub") # purse1 - Объект (экземпляр класса)
purse2 = Purse("Василий", "Иванович", "Иванов", "Сочи", "rub")

purse1.income(200)
purse1.transfer(purse2, 100)
try:
    purse1.withdraw(200)
except ValueError as e:
    print(e)

purse1.__balance = "200"
purse1.info()
purse2.info()

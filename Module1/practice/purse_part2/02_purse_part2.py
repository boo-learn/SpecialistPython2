class Purse:
    def __init__(self, name, surname, second_name, city, currency):  # конструктор -
        # ф-ция вызываемая автоматически при создании объекта
        self.owner_name = name
        self.owner_surname = surname
        self.owner_second_name = second_name
        self.owner_city = city# Свойства - переменные внутри класса
        self.__balance = 0
        self.currency = currency
        self.history = {1 : f"init_operation-1 {self.__balance}"}
        self.status = True

    def income(self, summa):
        self.__balance += summa
        self.log_history("income", summa)

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= summa
        self.log_history("withdraw", summa)

    def transfer(self, other_purse, summa):
        self.withdraw(summa)
        other_purse.income(summa)

    def info(self): # метод - функция внутри класса
        # self - ссылка на объект, для которого был вызван данный метод
        print(f"Purse| owner:{self.owner_surname} {self.owner_name} balabce:{self.__balance} {self.currency}")

    def log_history(self, operation, new_value):
        i = 0
        for el in self.history.keys():
            if el > 0:
                i = el
        i += 1
        print(i+1)
        self.history[i] = f"{operation} {self.__balance}"

    def show_history(self):
        print(self.history)



purse1 = Purse("Иван", "Иванов", "Петрович", "Москва", "rub") # purse1 <-- Объект(экземпляр класса)
purse2 = Purse("Василий", "Козлов", "Алексеевич", "Казань", "rub")
#print(purse1.history)
purse1.income(200)
purse1.info() # --> Purse.info(purse1)
purse2.info()
try:
    purse1.transfer(purse2, 400)
except ValueError as e:
    print(e)
# try:
#     purse1.withdraw(300)
# except ValueError as e:
#     print(e)
purse1.info() # --> Purse.info(purse1)
purse2.info()


purse1.show_history()

purse1.show_history()

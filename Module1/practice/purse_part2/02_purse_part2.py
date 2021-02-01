class Purse:
    def __init__(self, name, sername, town, currency):  # конструктор -
        # ф-ция вызываемая автоматически при создании объекта
        self.owner_name = name  # Свойства - переменные внутри класса
        self.owner_sername = sername
        self.owner_town = town
        self.__balance = 0
        self.currency = currency
        self.__operation = []

    def income(self, summa):
        self.__balance += summa
        self.__operation.append(f"Поступление {summa}")

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= summa
        self.__operation.append(f"Снятие {summa}")

    def transfer(self, other_purse, summa):
        self.withdraw(summa)
        other_purse.income(summa)
        self.__operation.append(f"перевод {summa} на {other_purse}")

    def save_story(self, __operation):
        pass

    def info(self): # метод - функция внутри класса
        # self - ссылка на объект, для которого был вызван данный метод
        print(f"Purse| owner:{self.owner_name} {self.owner_sername} |  Город {self.owner_town} | balabce:{self.__balance} {self.currency} ")
        print(f"Story {self.__operation}")


purse1 = Purse("Иван", "Грозный", "Москва", "rub")  # purse1 <-- Объект(экземпляр класса)
purse2 = Purse("Василий", "Горелый", "Питер", "rub")
purse1.income(200)
purse1.info() # --> Purse.info(purse1)
purse2.info()
try:
    purse1.transfer(purse2, 100)
except ValueError as e:
    print(e)
# try:
#     purse1.withdraw(300)
# except ValueError as e:
#     print(e)
purse1.info() # --> Purse.info(purse1)
purse2.info()

print()

# 1. Инкапсуляция
# 1.1. Объединение свойств и методов в одном контейнере
# 1.2. Сокрытие внутренней реализации от пользователя класса
# 2. Полиморфизм
# 3. Наследование

class Purse:
    def __init__(self, surname, name, name2, town, currency):  # конструктор -
        # ф-ция вызываемая автоматически при создании объекта
        self.owner_surname = surname
        self.owner_name = name  # Свойства - переменные внутри класса
        self.owner_name2 = name2
        self.owner_town = town
        self.__balance = 0
        self.currency = currency

    def income(self, summa):
        self.__balance += summa

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= summa

    def transfer(self, other_purse, summa):
        self.withdraw(summa)
        other_purse.income(summa)

    def info(self):  # метод - функция внутри класса
        # self - ссылка на объект, для которого был вызван данный метод
        print(f"Purse| owner:{self.owner_surname} {self.owner_name} balabce:{self.__balance} {self.currency}")

    def history(self, operation):
        
purse1 = Purse("Иван", "rub")  # purse1 <-- Объект(экземпляр класса)
purse2 = Purse("Василий", "rub")

purse1.income(200)

purse1.info()  # --> Purse.info(purse1)
purse2.info()
try:
    purse1.transfer(purse2, 400)
except ValueError as e:
    print(e)
# try:
#     purse1.withdraw(300)
# except ValueError as e:
#     print(e)
purse1.info()  # --> Purse.info(purse1)
purse2.info()

# 1. Инкапсуляция
# 1.1. Объединение свойств и методов в одном контейнере
# 1.2. Сокрытие внутренней реализации от пользователя класса
# 2. Полиморфизм
# 3. Наследование

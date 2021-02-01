class Purse:
    def __init__(self, name, patronymic, lastname, currency):  # конструктор -
        # ф-ция вызываемая автоматически при создании объекта
        self.owner_name = name  # Свойства - переменные внутри класса
        self.owner_lastname = lastname
        self.owner_patronymic = patronymic
        self.__is_blocked = False
        self.__history = list()
        self.__balance = 0
        self.currency = currency

    def income(self, summa):
        self.__balance += summa
        self.__history.append({"type": "income",
                               "value": summa})

    def withdraw(self, summa):
        if summa > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= summa
        self.__history.append({"type": "withdraw",
                               "value": summa})

    def transfer(self, other_purse, summa):
        self.withdraw(summa)
        other_purse.income(summa)
        self.__history.append({"type": "transfer",
                               "beneficiary": f"{other_purse.owner_name} {other_purse.owner_lastname}",
                               "value": summa})

    def info(self):  # метод - функция внутри класса
        # self - ссылка на объект, для которого был вызван данный метод
        print(f"Purse| owner:{self.owner_name} {self.owner_lastname} balance:{self.__balance} {self.currency}")

    def print_history(self, opera_type):
        defined_operations = set(["transfer", "withdraw", "income"])
        if not (opera_type in defined_operations):
            raise ValueError("incorrect operation name")

        def check(f):
            return f["type"] == opera_type

        print(list(filter(check, self.__history)))
        # print(list(self.__history))

purse1 = Purse("Иван", "Никифорович", "Бездомный", "rur")  # purse1 <-- Объект(экземпляр класса)
purse2 = Purse("Василий", "Иванович", "Чапаев", "rub")
purse1.income(200)
purse1.income(250)
purse1.income(200)
purse1.withdraw(100)
purse1.print_history("income")

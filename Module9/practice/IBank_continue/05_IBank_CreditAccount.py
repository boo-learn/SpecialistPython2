from Accountv2 import Account


# FIXME: допишите текущий класс, чтобы проходили все тесты для него ("TestCreditAccount")
class CreditAccount(Account):
    inc_commission = 5  # увеличенная комиссия при -балансе

    def __init__(self, name, second_name, surname, passport8, phone_number, start_balance=0, negative_limit=-100):
        # Account.__init__(self, name, second_name, surname, passport8, phone_number, start_balance)
        super().__init__(name, second_name, surname, passport8, phone_number, start_balance)
        self.negative_limit = negative_limit
        self.__in_archive = False  # в архиве

    @property
    def in_archive(self):
        return self.__in_archive

    def to_archive(self):
        """
        Убрать в архив
        """
        if self.balance < 0:
            raise ValueError('Нельзя убрать счет с отрицательным балансом в архив')
        self.balance = 0
        self.__in_archive = True

    def restore(self):
        """
        Восстановить из архива
        """
        self.__in_archive = False

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "<К>Иванов И.П. баланс: 100 руб."
        """
        # s = Account.__repr__(self)
        s = super().__repr__()
        return f"<К>{s}"

    def full_info(self):
        s = super().full_info()
        return f"<K>{s}"

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        try:
            super().withdraw(amount)
        except ValueError:
            if self.balance - amount * (1 + self.commission / 100) < self.negative_limit:
                raise ValueError('Превышен лимит')
            if self.balance < 0:
                self.balance -= amount * (1 + (self.commission + 3) / 100)
            else:
                self.balance -= amount * (1 + self.commission / 100)
            pass


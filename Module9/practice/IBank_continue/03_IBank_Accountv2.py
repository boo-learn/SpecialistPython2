from ... import AccountBase


class Account(AccountBase):
    commission = 2

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError("Недостаточно средств")
        self.balance -= amount * (1 + self.commission / 100)

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance < (amount * (1 + self.commission / 100)):
            raise ValueError("Недостаточно средств")
        self.balance -= amount * (1 + self.commission / 100)
        target_account.balance += amount

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.surname} {self.name[0]}.{self.second_name[0]}. баланс: {self.balance} руб."

    def full_info(self):
        # Иванов Иван Петрович баланс: 21283 руб.телефон: +7 - 912 - 622 - 11 - 22
        return f"{self.surname} {self.name}.{self.second_name}. баланс: {self.balance} руб. т.{self.phone_number}"
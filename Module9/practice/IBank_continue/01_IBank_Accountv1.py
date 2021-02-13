from classes.AccountBase import AccountBase


class Account(AccountBase):
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
        self.balance -= amount

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance < amount:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        target_account.balance += amount

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.surname} {self.name[0]}.{self.second_name[0]}. баланс: {self.balance} руб."

    def full_info(self):
        # Иванов Иван Петрович баланс: 21283 руб.телефон: +7 - 912 - 622 - 11 - 22
        return f"{self.surname} {self.name}.{self.second_name}. баланс: {self.balance} руб. т.{self.phone_number}"


if __name__ == "__main__":
    # Выполняем минимальное тестирование:
    acc = Account("Иван", "Петрович", "Вознесенский", 12345678, 79006001020)
    print(acc)
    acc.deposit(500)
    print(acc)
    try:
        acc.withdraw(600)
    except ValueError as e:
        print(e)
    print(acc)
    try:
        acc.withdraw(400)
    except ValueError as e:
        print(e)
    print(acc)
    acc2 = Account("Алексей", "Васильевич", "Козликов", 12345679, 79006001122, start_balance=1200)
    print(acc2)
    acc2.transfer(acc, 1100)
    print(acc2)
    print(acc.full_info())
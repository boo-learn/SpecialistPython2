from generators import get_user_data
from abc import ABC, abstractmethod
import datetime

EMPLOYEE_PASSWORD = "123"


class AccountBase(ABC):
    def __init__(self, name, second_name, surname, passport8, phone_number, start_balance=0, archive=False):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance
        self.archive = archive
        self.transaction_history = []

    @abstractmethod
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        pass


class Account(AccountBase):
    comission = 2

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        Transaction(self, target_account, amount, Account.comission)

    def full_info(self):
        # Иванов Иван Петрович баланс: 21283 руб.телефон: +7 - 912 - 622 - 11 - 22
        return f"{self.surname} {self.name}.{self.second_name}. баланс: {self.balance} руб. т.{self.phone_number}"

    def put(self, amount):
        if amount <= 5000:
            self.balance += amount
        else:
            raise ValueError("Разовое пополнение более 5К невозможно")

    def get(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств для снятия")

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.surname} {self.name[0]}.{self.second_name[0]}. баланс: {self.balance} руб."


class CreditAccount(Account):
    def __init__(self, name, second_name, surname, passport8, phone_number, start_balance=0, negative_limit=-100):
        # Account.__init__(self, name, second_name, surname, passport8, phone_number, start_balance)
        super().__init__(name, second_name, surname, passport8, phone_number, start_balance)
        self.negative_limit = negative_limit

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        s = Account.__repr__(self)
        # super().__repr__()
        return f"<К>{s}"

    def get(self, amount):
        if self.balance + abs(self.negative_limit) >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств для снятия")

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance >= 0:
            super().transfer(target_account, amount)
        else:
            Transaction(self, target_account, amount, 5)


class Transaction:
    def __init__(self, account_from=None, account_to=None, amount=0, comission=0):
        self.account_from = account_from
        self.account_to = account_to
        self.amount = amount
        self.comission = round(float(amount) * comission / 100, 2)
        self.transaction_success = False
        self.move_money()
        self.date_time = datetime.datetime.now()
        if account_from is not None:
            account_from.transaction_history.append(self)
        if account_to is not None:
            account_to.transaction_history.append(self)

    def move_money(self):
        get_success = True
        put_success = True
        if self.account_from is not None:
            try:
                self.account_from.get(float(self.amount) + float(self.comission))
                accounts[0].put(self.comission)
            except ValueError as e:
                get_success = False
                print(e)
        if get_success:
            if self.account_to is not None:
                try:
                    self.account_to.put(float(self.amount))
                except ValueError as e:
                    put_success = False
                    print(e)
            if not put_success:
                self.account_from.put(float(self.amount) + float(self.comission))
                accounts[0].get(float(self.comission))
                return
            self.transaction_success = True

    def __repr__(self):
        if self.transaction_success:
            s = "(Успешно)"
        else:
            s = "(Транзакция отклонена)"
        if self.account_from is not None and self.account_to is not None:
            return f"{self.date_time} перевод на счет {self.account_to.surname} {self.account_to.name[0]}. сумма {self.amount} руб. комиссия {self.comission} {s}"

        if self.account_from is not None:
            return f"{self.date_time} снятие в банкомате {self.amount} руб. комиссия {self.comission} {s}"

        if self.account_to is not None:
            return f"{self.date_time} внесение через банкомат {self.amount} руб. комиссия {self.comission} {s}"


def close_account():
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    passport = int(input("client passport: "))
    account = get_account_by_password(accounts, passport)
    if account is None:
        print("Not found")
        return
    accounts.remove(account)


def view_accounts_list():
    """
    Отображение всех клиентов банка в виде нумерованного списка
    """
    for number, account in enumerate(accounts, 1):
        print(f"{number}. {account}")


def view_account_by_passport():
    passport = int(input("client passport: "))
    account = get_account_by_password(accounts, passport)
    if account is None:
        print("Not found")
    print(account.full_info())


def view_client_account(account):
    """
    Узнать состояние своего счета
    """
    pass


def put_account(account):
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    amount = int(input("money put:"))
    Transaction(None, account, amount, 0)


def withdraw(account):
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    amount = int(input("money get:"))
    Transaction(account, None, amount, 0)


def transfer(account):
    """
    Перевести на счет другого клиента по номеру телефона
    """
    view_accounts_list()
    account_to = input('введите порядковый номер счета получателя ')
    index_account_to = int(account_to)
    if 1 <= index_account_to <= len(accounts):
        amount = input('введите сумму ')
        account.transfer(accounts[int(account_to) - 1], amount)
    else:
        print("Нет такого счета")

def print_transaction_history(account):
    for number, transaction in enumerate(account.transaction_history, 1):
        print(f"{number}. {transaction}")

def create_new_account():
    # print("Укажите данные клиента")
    # name = input("Имя:")
    # second_name = input("Отчество:")
    # surname = input("Фамилия:")
    # passport = input("Номер паспорта: ")
    # phone_number = input("Номер телефона: ")
    # Если лень каждый раз вводить - воспользуйтесь функцией генератором
    name, surname, second_name, passport, phone_number = get_user_data()
    new_account = Account(name, surname, second_name, passport, phone_number)
    accounts.append(new_account)
    # Account(*get_user_data())
    # TODO: тут создаем новый аккаунт пользователя account = ...
    #   и добавляем его в accounts.append(account)


def client_menu(account):
    while True:
        print(f"***********Меню клиента <{account.surname} {account.name[0]}.>*************")
        print("0. Посмотреть историю транзакций")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(":")
        if choice == "0":
            print_transaction_history(account)
        if choice == "1":
            view_client_account(account)
        elif choice == "2":
            put_account(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            transfer(account)
        elif choice == "5":
            return
    # input("Press Enter")


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            create_new_account()
        elif choice == "2":
            close_account()
        elif choice == "3":
            view_accounts_list()
        elif choice == "4":
            view_account_by_passport()
        elif choice == "5":
            return


def employee_access():
    """
    Проверяет доступ сотрудника банка, запрашивая пароль
    """
    password = input("Пароль: ")
    if password == EMPLOYEE_PASSWORD:
        return True
    return False


def get_account_by_password(accounts, passport):
    for account in accounts:
        if passport == account.passport8:
            return account
    return None


def client_access(accounts):
    """
    Находит аккаунт с введеным номером паспорта
    Или возвращает False, если аккаунт не найден
    """
    try:
        passport = int(input("Номер паспорта: "))
    except ValueError:
        return False
    return get_account_by_password(accounts, passport)


def start_menu():
    while True:
        print("Укажите вашу роль:")
        print("1. Сотрудник банка")
        print("2. Клиент")
        print("3. Завершить работу")

        choice = input(":")
        if choice == "3":
            break
        elif choice == "1":
            if employee_access():
                employee_menu()
            else:
                print("Указан неверный пароль, укажите роль и повторите попытку...")
        elif choice == "2":
            account = client_access(accounts)
            if account:
                client_menu(account)
            else:
                print("Указан несуществующий пасспорт, укажите роль и повторите попытку...")
        else:
            print("Указан некорректный пункт меню, повторите выбор...")


if __name__ == "__main__":
    accounts = [
        Account(" ", " ", "БАНК", 0, 0000000000, 0),
        Account("Иван", "Иванович", "Иванов", 12345678, 7900100100, 50000),
        Account("Петр", "Петрович", "Петров", 12345679, 7900100101, 500),
        Account("Сидор", "Сидорович", "Сидоров", 12345680, 7900100102, 500),
        CreditAccount("Мария", "Ивановна", "Иванова", 12345681, 7900100103, 1200, 500)
    ]
    start_menu()

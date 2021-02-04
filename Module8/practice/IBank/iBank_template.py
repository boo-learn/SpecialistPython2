# from generators import get_user_data
from abc import ABC, abstractmethod

EMPLOYEE_PASSWORD = "123"


class AccountBase(ABC):
    def __init__(self, name, second_name, surname, passport8, phone_number, start_balance=0):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

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


def close_account():
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    indexs = []
    passport = input('Введите номер паспорта счета ')
    for account in accounts:
        if account.passport8 == passport:
            index = accounts.index(account)
            indexs.append(index)
    for index in indexs:
        accounts.remove(index)

def view_accounts_list():
    """
        Отображение всех клиентов банка в виде нумерованного списка
        """
    for account in accounts:
        print(account)


def view_account_by_passport():
    pass


def view_client_account():
    """
    Узнать состояние своего счета
    """
    pass


def put_account():
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    pass


def withdraw():
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    pass


def transfer():
    """
    Перевести на счет другого клиента по номеру телефона
    """
    pass


def create_new_account():
    from generators import get_user_data
    tuple = get_user_data()
    name = tuple[0]
    second_name = tuple[1]
    surname = tuple[2]
    passport = tuple[3]
    phone_number = tuple[4]
    # TODO: тут создаем новый аккаунт пользователя account = ...
    #   и добавляем его в accounts.append(account)
    account = Account(name, second_name, surname, passport, phone_number, 100)
    accounts.append(account)
    return

    # print("Укажите данные клиента")
    # name = input("Имя:")
    # second_name = input("Отчество:")
    # surname = input("Фамилия:")
    # passport = input("Номер паспорта: ")
    # phone_number = input("Номер телефона: ")
    # # Если лень каждый раз вводить - воспользуйтесь функцией генератором
    # # name, surname, second_name, passport, phone_number = gen_user_data()


def client_menu(account):
    while True:
        print("***********Меню клиента <Иванов И.И.>*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Exit")
        choice = input(":")
        if choice == "1":
            view_client_account()
        elif choice == "2":
            put_account()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
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


def client_access(accounts):
    """
    Находит аккаунт с введеным номером паспорта
    Или возвращает False, если аккаунт не найден
    """
    try:
        passport = int(input("Номер паспорта: "))
    except ValueError:
        return False
    for account in accounts:
        if passport == account.passport8:
            return account

    return False


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

class Account(AccountBase):
    def transfer(self, target_account, amount):
         """
         Перевод денег на счет другого клиента
         :param target_account: счет клиента для перевода
         :param amount: сумма перевода
         :return:
         """
         if self.balance >= amount:
             self.balance -= amount
             target_account.balance += amount
         else:
             raise ValueError("Недостаточно средств")
         return

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.surname} {self.name[0]}.{self.second_name[0]}. баланс: {self.balance} руб. (паспорт {self.passport8})"


if __name__ == "__main__":
    accounts = []
    start_menu()

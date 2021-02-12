# from generators import get_user_data
from abc import ABC, abstractmethod

EMPLOYEE_PASSWORD = "123"

class AccountBase(ABC):
    def __init__(self, name, second_name, surname, passport8, phone_number, limit=0 ,start_balance=0):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.passport8 = passport8
        self.phone_number = phone_number
        self.limit = limit
        self.balance = start_balance
        self.inlist = []
        self.outlist = []
        self.translist = [] 
        self.komlist = [] 

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
    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        pass

    @abstractmethod
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"..."

    @abstractmethod
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."

###############################################################################################################################

class Account(AccountBase):
    def transfer(self, target_account, amount):
        self.withdraw(amount)
        k = 1
        if self.limit == 0:
            k = 2
        else:
            k = 5
        target_account.deposit( amount - ((amount/100.0) * k) )
        self.translist.append( amount ) 
        self.komlist.append( (amount/100.0) * k )

    def deposit(self, amount):
        self.balance += amount
        self.inlist.append(amount)
        
    def withdraw(self, amount):
        if amount > self.balance + self.limit:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        self.outlist.append(amount)

    def history(self):
    
        print("Поступления: ")
        for i in self.inlist:
            print(i)

        print("Списания: ")
        for j in self.outlist:
            print(j)
            
        print("Переводы: ")
        jj = 0
        for k in self.translist:
            print(k,' ком.', self.komlist[jj])
            jj += 1

        
    def full_info(self):
      if self.limit == 0:
        return f"{self.surname} {self.name} {self.second_name} " \
               f"баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"
      else:
        return f"K {self.surname} {self.name} {self.second_name} " \
               f"баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"
        
    def __repr__(self):
      if self.limit == 0:
        return f"{self.surname} {self.name[0]}.{self.second_name[0]}. баланс: {self.balance} руб."
      else:
        return f"K {self.surname} {self.name[0]}.{self.second_name[0]}. баланс: {self.balance} руб."

def close_account():
    """
    Закрыть счет клиента.
    Считаем, что оставшиеся на счету деньги были выданы клиенту наличными, при закрытии счета
    """
    try:
        passport = int(input("Номер паспорта: "))

    except ValueError:
        return False

    for account in accounts:
        if passport == account.passport8:
            account.withdraw(account.balance)
            arhaccounts.append(account)
            accounts.remove(account)
            break


def view_accounts_list():
    """
    Отображение всех клиентов банка в виде нумерованного списка
    """
    for account in accounts:
        print(account)


def view_kaccounts_list():
    """
    Отображение всех клиентов банка в виде нумерованного списка
    """
    for account in accounts:
        if account.balance < 0:
            print(account)


def view_arhaccounts_list():
    """
    Отображение всех клиентов банка в виде нумерованного списка
    """
    for account in arhaccounts:
        print(account)



def view_account_by_passport():
    try:
        passport = int(input("Номер паспорта: "))

    except ValueError:
        return False

    for account in accounts:
        if passport == account.passport8:
            print(account)
            break

def view_client_account(account):
    """
    Узнать состояние своего счета
    """
    print(account)


def put_account(account):
    """
    Пополнить счет на указанную сумму.
    Считаем, что клиент занес наличные через банкомат
    """
    amount = int(input("Сумма пополнения: "))
    account.deposit(amount)


def withdraw(account):
    """
    Снять со счета.
    Считаем, что клиент снял наличные через банкомат
    """
    amount = int(input("Сумма списания: "))
    account.withdraw(amount)


def transfer(account):
    """
    Перевести на счет другого клиента по номеру телефона
    """
    phone  = int(input("phone: "))
    amount = int(input("Сумма перевода: "))

    for account2 in accounts:
        if phone == account2.phone_number:
            print(account2)
            account.transfer(account2,amount)

def history(account):
    """
    история движений по счету
    """
    print('История движеий по счету:')
    account.history()


def create_new_account():
    print("Укажите данные клиента")
    name = input("Имя:")
    second_name = input("Отчество:")
    surname = input("Фамилия:")
    passport = input("Номер паспорта: ")
    phone_number = input("Номер телефона: ")
    limit = input("Размер максимального кредита: ")
    # name, surname, second_name, passport, phone_number = get_user_data()
    account = Account(name, surname, second_name, passport, phone_number,limit)
    # account = Account(*get_user_data())
    accounts.append(account)

def restore_account():
    try:
        passport = int(input("Номер паспорта для восстановления счета: "))

    except ValueError:
        return False

    for account in arhaccounts:
        if passport == account.passport8:
            print(account)
            accounts.append(account)
            arhaccounts.remove(account)
            break





def client_menu(account):
    while True:
        print(f"***********Меню клиента <{account.surname} И.И.>*************")
        print("1. Состояние счета")
        print("2. Пополнить счет")
        print("3. Снять со счета")
        print("4. Перевести деньги другому клиенту банка")
        print("5. Просмотр истории движения денежных средств по счету")
        print("6. Exit")
        choice = input(":")
        if choice == "1":
            view_client_account(account)
        elif choice == "2":
            put_account(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            transfer(account)
        elif choice == "5":
            history(account)
        elif choice == "6":
            return
    # input("Press Enter")


def employee_menu():
    while True:
        print("***********Меню сотрудника*************")
        print("1. Создать новый счет")
        print("2. Закрыть счет")
        print("3. Посмотреть список счетов")
        print("4. Посмотреть счет по номеру паспорта")
        print("5. Просмотр архивных счетов")
        print("6. Восстановления счета из архива")
        print("7. Просмотр всех счетов с отрицательным балансом")
        print("8. Exit")

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
            view_arhaccounts_list()
        elif choice == "6":
            restore_account()
        elif choice == "7":
            view_kaccounts_list()
        elif choice == "8":
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

def proclst(inp,eel):
        inp = eel
        inp = inp.split(',')
        inp = inp[1:]
        if len(inp) == 1 and inp[0] == '':
            return []
        else: return [float(item) for item in inp]

def proclst2(sss):
        sss = sss.replace('[', '')
        sss = sss.replace(']', '')
        return sss

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

    accounts = []
    # файлы должны быть созданы заранее
    f1 = open(r"C:\temp\accounts.txt",    'r')
    s1 = f1.readlines() 
    
    i = 0
    inlist = []
    outlist = []
    translist = [] 
    komlist = [] 

    for el in s1:

        if el[0:3] == 'IN ':
            inlist = proclst(inlist,el[0:-1])
        if el[0:3] == 'OUT':
            outlist = proclst(outlist,el[0:-1])
        if el[0:3] == 'TRA':
            translist = proclst(translist,el[0:-1])
        if el[0:3] == 'KOM':
            komlist = proclst(komlist,el[0:-1])
        if el[0:3] == 'ACC':
            newel = el[0:-1]
            newel = newel.split(',')
            acc = Account(newel[1], newel[2], newel[3], float(newel[4]), float(newel[5]),float(newel[6]), float(newel[7]))
            acc.inlist = inlist[:]
            acc.outlist = outlist[:]
            acc.translist = translist[:] 
            acc.komlist = komlist[:] 

            accounts.append(acc)
            inlist = []
            outlist = []
            translist = [] 
            komlist = [] 

            
    # accounts = [
        # Account("Иван", "Петрович", "Алексеев", 12345678, 89001001020,0, 500),
        # Account("Петр", "Алексеевич", "Иванов", 12345679, 89001001021),
        # Account("Иван1", "Петрович1", "Алексеев1", 32345678, 89001001023,100, 500),
        # Account("Петр1", "Алексеевич1", "Иванов1", 22345679, 89001001022,0,23),
    # ]

    f1.close()

    arhaccounts = []
    
    # файлы должны быть созданы заранее
    f3 = open(r"C:\temp\arhaccounts.txt",    'r')
    s1 = f3.readlines() 
    
    i = 0
    inlist = []
    outlist = []
    translist = [] 
    komlist = [] 

    for el in s1:

        if el[0:3] == 'IN ':
            inlist = proclst(inlist,el[0:-1])
        if el[0:3] == 'OUT':
            outlist = proclst(outlist,el[0:-1])
        if el[0:3] == 'TRA':
            translist = proclst(translist,el[0:-1])
        if el[0:3] == 'KOM':
            komlist = proclst(komlist,el[0:-1])
        if el[0:3] == 'ACC':
            newel = el[0:-1]
            newel = newel.split(',')
            acc = Account(newel[1], newel[2], newel[3], float(newel[4]), float(newel[5]),float(newel[6]), float(newel[7]))
            acc.inlist = inlist[:]
            acc.outlist = outlist[:]
            acc.translist = translist[:] 
            acc.komlist = komlist[:] 

            arhaccounts.append(acc)
            inlist = []
            outlist = []
            translist = [] 
            komlist = [] 

            f3.close()

    start_menu()

    f2 = open(r"C:\temp\accounts.txt",'w')
    f4 = open(r"C:\temp\arhaccounts.txt",'w')

    for acc in accounts:
        sss = proclst2(str(acc.inlist))
        f2.write('IN ,' + sss + '\n')
        sss = proclst2(str(acc.outlist))
        f2.write('OUT,' + sss + '\n')
        sss = proclst2(str(acc.translist))
        f2.write('TRA,' + sss + '\n')
        sss = proclst2(str(acc.komlist))
        f2.write('KOM,' + sss + '\n')
        f2.write('ACC,' + str(acc.name) + ',' + str(acc.second_name) + ',' + str(acc.surname) + ',' + str(acc.passport8) + ',' + str(acc.phone_number) + ',' + str(acc.limit) + ',' + str(acc.balance)  + '\n')

    f2.close()
    
    for acc in arhaccounts:
        sss = proclst2(str(acc.inlist))
        f4.write('IN ,' + sss + '\n')
        sss = proclst2(str(acc.outlist))
        f4.write('OUT,' + sss + '\n')
        sss = proclst2(str(acc.translist))
        f4.write('TRA,' + sss + '\n')
        sss = proclst2(str(acc.komlist))
        f4.write('KOM,' + sss + '\n')
        f4.write('ACC,' + str(acc.name) + ',' + str(acc.second_name) + ',' + str(acc.surname) + ',' + str(acc.passport8) + ',' + str(acc.phone_number) + ',' + str(acc.limit) + ',' + str(acc.balance)  + '\n')

    f4.close()

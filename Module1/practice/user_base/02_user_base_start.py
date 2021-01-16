import os
import hashlib

class User:
    max_id = 0
    # конструктор
    def __init__(self, name, surname, username, password):
        User.max_id += 1
        self.id = User.max_id
        self.name = name
        self.surname = surname
        self.username = username
        self.password = self.get_hash(password)

    def get_hash(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

        return salt + key

    def check_password(self, password):
        salt = self.password[:32]  # 32 is the length of the salt
        key = self.password[32:]
        new_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            salt,
            100000
        )
        return new_hash == key

    # Метод - функция внутри класса
    def show(self):
        print(f"id:{self.id}: {self.surname} {self.name[0]}. [{self.username}]")


users = [
    User("Иван", "Иванов", "ivan", "123"),
    User("Петр", "Петров", "petr", "234"),
    User("Алексей", "Уткин", "alex", "do-)"),
]

while True:
    print("Меню")
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("3. Список пользователей")
    print("4. Редактирование пользователя")
    print("5. Выход")
    choice = input(": ")
    if choice == "1":
        print("****Добавление нового пользователя****")
        name = input("name: ")
        surname = input("surname: ")
        username = input("username: ")
        password = input("password: ")
        user = User(name, surname, username, password)
        users.append(user)
        print(f"Пользователь {user.surname} {user.name} {user.id} добавлен в базу")
    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))
        for cur_us in users:
            if cur_us.id == id:
                users.remove(cur_us)
                print(f"Пользователь {cur_us.surname} {cur_us.name} с id:{id} удален из базы")
                break
        else:
            print(f"Пользователь с id: {id} не найден")

    elif choice == "3":
        print("****Список всех пользователей****")
        for num, user in enumerate(users, 1):
            print(f'{num}: ', end=' ')
            user.show()

    elif choice == "4":
        print("****Редактирование пользователя****")
        id = int(input('id: '))
        ...
        print("Какой параметр хотите изменить?")
        print("1. name")
        print("2. surname")
        print("3. username")
        print("4. password")
        param_number = input(': ')
        if param_number == '1':
            new_name = input(f"Старое имя {name}. Новое имя: ")
            ...
        elif param_number == '2':
            new_surname = input(f"Старая фамилия {surname}. Новая фамилия: ")
            ...
        elif param_number == '3':
            ...
        elif param_number == '4':
            ...
        else:
            ...
        # print(f"Пользователь с id: {id} не найден")
    elif choice == "5":
        print("GoodBy -(")
        break

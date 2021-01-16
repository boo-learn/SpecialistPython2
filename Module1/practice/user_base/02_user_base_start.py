# admin-b@specialist.ru
# +7(495)780-47-48

id = 0
users = {}

class User:
    def init(self):
        self.name = ''
        self.surname = ''
        self.username = ''
        self.password = ''

    def add(self, name, surname, username, password):
        self.id = id + 1
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        users.update({
            self.id: {
            'name': self.name,
            'surname': self.surname,
            'username': self.username,
            'password': self.password
        }})

    def delete(self, id):
        users.pop(id)

def main():
    while True:
        user = User
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
            user.add(name, surname, username, password)
            print(f"Пользователь {surname} {name} добавлен в базу")
        elif choice == "2":
            print("****Удаление пользователя****")
            id = int(input('id: '))
            user = User
            user.delete(id)
            print(f"Пользователь {user.surname} {user.name} с id:{id} удален из базы")
            # print(f"Пользователь с id: {id} не найден")

        elif choice == "3":
            print("****Список всех пользователей****")
            for i in users:
                print(f"{i}: {i['name'][0]} {i['surname']}")

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
            print("GoodBye -(")
            break


if __name__ == '__main__':
    main()

# admin-b@specialist.ru
# +7(495)780-47-48
import password_hash


class User:
    max_id = 0
    users = {}

    def __init__(self, id):
        self.id = id
        self.name = User.users[id]['name']
        self.surname = User.users[id]['surname']
        self.username = User.users[id]['username']
        self.password = User.users[id]['password']

    @staticmethod
    def add(name, surname, username, password):
        User.max_id += 1
        User.users.update({
            User.max_id: {
                'name': name,
                'surname': surname,
                'username': username,
                'password': password_hash.get_hash(password)
            }
        })
        return(f"Пользователь {surname} {name} добавлен в базу")

    @staticmethod
    def delete(id):
        if User.users.get(id) is not None:
            user = User(id)
            User.users.pop(id)
            return f"Пользователь {user.surname} {user.name} с id:{id} удален из базы"
        return f"Пользователь с id: {id} не найден"


def main():
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
            print(User.add(input("name: ").capitalize(), input("surname: ").capitalize(), input("username: "), input("password: ")))

        elif choice == "2":
            print("****Удаление пользователя****")
            id = int(input('id: '))
            print(User.delete(id))

        elif choice == "3":
            print("****Список всех пользователей****")
            for num, user in enumerate(User.users, 1):
                user = User(user)
                print(f"{num}. {user.id}: {user.name[0]}. {user.surname} [{user.username}]")

        elif choice == "4":
            print("****Редактирование пользователя****")
            id = int(input('id: '))
            if User.users.get(id) is not None:
                user = User(id)
                print("Какой параметр хотите изменить?")
                print("1. name")
                print("2. surname")
                print("3. username")
                print("4. password")
                param_number = input(': ')
                if param_number == '1':
                    new_name = input(f"Старое имя {user.name}. Новое имя: ")
                    user.name = new_name
                elif param_number == '2':
                    new_surname = input(f"Старая фамилия {user.surname}. Новая фамилия: ")
                    user.surname = new_surname
                elif param_number == '3':
                    new_username = input(f"Старое имя пользователя {user.username}. Новаое имя пользователя: ")
                    user.username = new_username
                elif param_number == '4':
                    new_password = input(f"Новый пароль: ")
                    user.password = password_hash.get_hash(new_password)
            else:
                print(f"Пользователь с id: {id} не найден")

        elif choice == "5":
            print("GoodBye -(")
            break


if __name__ == '__main__':
    main()

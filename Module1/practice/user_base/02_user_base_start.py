
NAME = "name"
SURNAME = "surname"
USERNAME = "username"
PASSWORD = "password"

users = {}
current_id = 0

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

        curent_user = {NAME:name, SURNAME:surname, USERNAME:username, PASSWORD:password}
        current_id += 1
        users[current_id] = curent_user

        print(f"Пользователь {surname} {name} добавлен в базу")

    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))

        curent_user = users.get(id)

        if curent_user == None :
            print(f"Пользователь с id: {id} не найден")

        else :
            del users[id]
            surname = curent_user[SURNAME]
            name=curent_user[NAME]

            print(f"Пользователь {surname} {name} с id:{id} удален из базы")

    elif choice == "3":
        print("****Список всех пользователей****")

        for key in users :
            curent_user = users[key]
            name = curent_user[NAME]
            surname = curent_user[SURNAME]
            username = curent_user[USERNAME]

            print(f"{key}: {name[0]} {surname} [username]")

    elif choice == "4":
        print("****Редактирование пользователя****")
        id = int(input('id: '))

        curent_user = users.get(id)

        if curent_user == None:
            print(f"Пользователь с id: {id} не найден")
            continue

        name = curent_user[NAME]
        surname = curent_user[SURNAME]
        username = curent_user[USERNAME]
        password = curent_user[PASSWORD]

        print("Какой параметр хотите изменить?")
        print("1. name")
        print("2. surname")
        print("3. username")
        print("4. password")
        param_number = input(': ')
        if param_number == '1':
            new_name = input(f"Старое имя {name}. Новое имя: ")
            curent_user[NAME] = new_name

        elif param_number == '2':
            new_surname = input(f"Старая фамилия {surname}. Новая фамилия: ")
            curent_user[SURNAME] = new_surname

        elif param_number == '3':
            new_username = input(f"Старый username  {username}. Новый username: ")
            curent_user[USERNAME] = new_username

        elif param_number == '4':
            new_password = input(f"Старый праоль  {password}. Новый пароль: ")
            curent_user[PASSWORD] = password
        else:
            continue

        users[id] = curent_user

    elif choice == "5":
        print("GoodBy -(")
        break

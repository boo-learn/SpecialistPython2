users =[]
p_id = 0

while True:
    p_id = p_id + 1
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
        user = {"id":p_id,"name":name,"surname":surname,"username":username,"password":password}
        users.append(user)
        ...
        # print(f"Пользователь {surname} {name} добавлен в базу")
    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))
        for cuser in users:
            if cuser['id'] == id:
                users.remove(cuser)
                break
        else:
                print(f"user not found {id}")
        # print(f"Пользователь {surname} {name} с id:{id} удален из базы")
        # print(f"Пользователь с id: {id} не найден")

    elif choice == "3":
        print("****Список всех пользователей****")
        ...

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

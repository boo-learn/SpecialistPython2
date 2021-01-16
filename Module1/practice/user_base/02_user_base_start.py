# список пользователей
list_users = []
# словарь пользователя

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
        # поиск мах id
        max_id = 0
        for find_user in list_users:
            if find_user['id'] > max_id:
                max_id = find_user['id']
                print("max_id:", max_id)
        #
        dic_user = {}
        dic_user['id'] = max_id + 1
        dic_user['name'] = name
        dic_user['surname'] = surname
        dic_user['username'] = username
        dic_user['password'] = password
        dic_user['name'] = name
        list_users.append(dic_user)
        print(f"Пользователь {surname} {name} добавлен в базу")
   #     print(list_users)
    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))
        surname = ''
        for index, item in enumerate(list_users):
            if item['id'] == id:
                surname = item['surname']
                name = item['name']
                list_users.pop(index)
        if surname:
            print(f"Пользователь {surname} {name} с id:{id} удален из базы")
        else:
            print(f"Пользователь с id: {id} не найден")

    elif choice == "3":
        print("****Список всех пользователей****")
        ...
        # 12: Иванов И. [vanyok]
        for item in list_users:
            print(f"{item['id']}: {item['surname']} {item['name'][0]}. [{item['username']}]")

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

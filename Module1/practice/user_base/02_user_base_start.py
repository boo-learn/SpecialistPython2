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
        ...
        # print(f"Пользователь {surname} {name} добавлен в базу")
    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))
        ...
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

        ####
        import uuid
user = dict();
users = []
import random
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1
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
        id = uuid.uuid1()
       # user["id"] = xrange(20)
        user["Name"] = name
        user["Surname"] = surname
        user["Username"] = username
        user["Password"] = password
        unique_sequence = uniqueid()
        id = next(unique_sequence)
        user["id"] = id
        users.append(user)
        print(f"Пользователь {surname} {name} {id} добавлен в базу")
    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))
        for cur_us in users:
         if (cur_us['id'] == id):
             users.remove(cur_us)

    elif choice == "3":
        print("****Список всех пользователей****")
        for userIt in users:
            print(userIt)

    elif choice == "4":
        print("****Редактирование пользователя****")
        id = int(input('id: '))


        print("Какой параметр хотите изменить?")
        print("1. name")
        print("2. surname")
        print("3. username")
        print("4. password")
        param_number = input(': ')
        if param_number == '1':
            new_name = input(f"Старое имя {name}. Новое имя: ")
            for current_user in users:
                if (current_user["id"] == id):
                    current_user["name"] = new_name
        elif param_number == '2':
            new_surname = input(f"Старая фамилия {surname}. Новая фамилия: ")
            if (current_user["id"] == id):
                current_user["surnamename"] = surname
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


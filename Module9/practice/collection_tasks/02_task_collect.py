# Каждый ученик в классе изучает либо английский, либо французский, либо оба этих языка.
# У классного руководителя есть списки учеников, изучающих английский и французский языки.
# Помогите ему выяснить, сколько учеников в классе изучают только один язык.

# Входные данные:
# Для каждого ученика известны: Имя Фамилия и список изучаемых языков

# Для решения задачи подберите наиболее удобную структуру.
# Выведите: учеников, изучающих только один язык

# TODO: your code here...


####

import  collections


class Student:
    def __init__(self,name, surname,is_english,is_german):
        self.name = name
        self.surname = surname
        self.is_english = is_english
        self.is_german = is_german


student1 = Student("Ivan","Petrovich",1,0)
student2 = Student("Leha","Sidorovich",1,0)
student3 = Student("Yuri","Germanovich",1,0)
student4 = Student("Tanya","Olegovna",1,1)

col =[]

col.append(student1)
col.append(student2)
col.append(student3)
col.append(student4)


for el in col:
    if ((el.is_english + el.is_german)==1):
        print(el.name)

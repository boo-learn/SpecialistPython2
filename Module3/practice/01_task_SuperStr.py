# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой. Считать, что пустая строка не содержит повторов.

# 2. метод is_palindrom (), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.


class SuperStr(str):
    def __init__(self,str):
        self.str=str
    def is_repeatance(self,s):
        if not isinstance(s,str):
            return False

    def is_palindrom(self):
        if self.str == "":
            return True
        long_str=len(self.str)//2
        return self.str[0:long_str] == self.str[long_str+1:]

word=SuperStr('11011')
print(word.is_palindrom())

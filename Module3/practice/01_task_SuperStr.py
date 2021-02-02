# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой. Считать, что пустая строка не содержит повторов.

# 2. метод is_palindrom (), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

class SuperStr(str):
    def is_repeatance(self, s):
        if type(s) is not str:
            return False

        str_len = len(self)
        count = self.count(s)
        return len(s) * count == str_len

ss = SuperStr("abcabcabcabc")

print(ss)
print(ss.is_repeatance("abc"))

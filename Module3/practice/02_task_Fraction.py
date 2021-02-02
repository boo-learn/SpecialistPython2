# Задание "Простые дроби"

# Сюда отправляем задание с классом дроби

class Fraction:
    def __init__(self, str):
        self.__number = list(str)
        if self.__number[0] == '-':
            self.__number[1] = '-' + self.__number[1]
            self.__number.pop(0)
        for el in self.__number:
            if el in [' ', '/']:
                self.__number.remove(el)
        self.__number = list(map(int, self.__number[:]))


    # кривой косой
    def __add__(self, other):
        print((self.__number[0] + self.__number[1] / self.__number[2]) + (other.__number[0] + other.__number[1] / other.__number[2]))

    def show(self):
        return f"{self.__number[0]} {self.__number[1]}/{self.__number[2]}"

oper1 = Fraction('-2 3/5')
oper2 = Fraction('4 3/5')

print(oper1.show())
print(oper2.show())

print(oper1+oper2)

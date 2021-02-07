# класс для работы с денежными суммами.
class Money:
    def __init__(self, rub=0, cop=0):
        self._amount = rub * 100 + cop

    def __repr__(self):
        rub = self._amount // 100
        cop = self._amount % 100
        return f"{rub}руб. {cop}коп."

    def __add__(self, other):
        return Money(self._amount + other._amount)

    def __sub__(self, other):
        return Money(self._amount + other._amount)

    def __eq__(self, other):
        return self._amount == other._amount

    def __gt__(self, other):
        return self._amount > other._amount

    def __lt__(self, other):
        return self._amount < other._amount

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        if not isinstance(other,(int,float)):
            raise ValueError("Cant multiply with non-number")
        
#
# Реализовать:
#
# сложение
# вычитание
# умножение на целое число
# сравнение (больше, меньше, равно, не равно)

# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1)  # 21руб 20коп
# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

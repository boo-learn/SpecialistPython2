# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
import random
def gen_list(n, at= -20, till=20):
    return [random.randint(at, till) for _ in range(n)]

summa = 0
a = -5
b = 15
array = gen_list(10)
for el in array:
    if el > a and el < b:
        summa += el

print(array)
print(summa)

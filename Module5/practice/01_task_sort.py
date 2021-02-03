# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

import random
def gen_list(n, at= -20, till=20):
    return [random.randint(at, till) for _ in range(n)]

summa = 0
a = 2
array = gen_list(10)
for el in array:
    if el > a:
        summa += el

print(array)
print(summa)

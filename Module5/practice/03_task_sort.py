# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
import random
from bubble import bubble

def gen_list(n, at= -20, till=20):
    return [random.randint(at, till) for _ in range(n)]

array = gen_list(20)
print(array)
bubble(array)

print(array[:10:-1])
print(sum(array[:10:-1]))

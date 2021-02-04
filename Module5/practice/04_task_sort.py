# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
import random
from bubble import bubble

def gen_list(n, at= -20, till=20):
    return [random.randint(at, till) for _ in range(n)]

array = gen_list(20)
print(array)

array_abs = list(map(abs, array))
bubble(array_abs)

print(array_abs[:10:-1])
print(sum(array_abs[:10:-1]))

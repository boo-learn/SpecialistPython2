# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
from random import randint
def gen_list(count):
    arr = []
    for i in range(count):
        arr.append(randint(1, 99))
    return arr

def list_sum(a, arr):
    n=0
    for elm in arr:
        if int(elm) > a:
            n = n + int(elm)
    return n


A = int(input('Введите число  А\n'))
print()
arr = gen_list(50)

print(arr)
print(list_sum(A, arr))

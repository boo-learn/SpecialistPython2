# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
from random import randint
def gen_list(count):
    arr = []
    for i in range(count):
        arr.append(randint(1, 99))
    return arr

def list_sum(a, b, arr):
    n=0
    for elm in arr:
        if int(elm) > a and int(elm)<b:
            n = n + int(elm)
    return n

arr = gen_list(50)
print(arr)

A = int(input('Введите число  A\n'))
B = int(input('Введите число  B\n'))


print(list_sum(A, B, arr))




# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
from random import randint
def gen_list(count):
    arr = []
    for i in range(count):
        arr.append(randint(1, 99))
    return arr

def bbl(arr):
    n=len(arr)
    for elm in arr:
        for i, elm in enumerate(arr[0:len(arr)-1]):
            if int(elm) > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    arr = arr[::-1]
    return arr

def big_sum(arr):
    n = 0
    for elm in (arr[0:10]):
        n = n + int(elm)
    return n


arr = gen_list(100)
print(arr)
arr = bbl(arr)
print(arr)
arr = big_sum(arr)
print(arr)

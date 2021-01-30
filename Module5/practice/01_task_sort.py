# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

from sort_lib import gen_list
from quick_sort import quick_sort



def test1():
    arr = quick_sort(gen_list(10))
    A = 5

    summ = sum([i for i in arr if i > A])

    print(f'МАССИВ: {arr}')
    print(f'СУММА: {summ}')
    

if __name__ == '__main__':
    test1()

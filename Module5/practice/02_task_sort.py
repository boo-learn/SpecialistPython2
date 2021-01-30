# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
from sort_lib import gen_list
from quick_sort import quick_sort


def test2():
    arr = quick_sort(gen_list(10))
    A = 3
    B = 150000

    summ = sum([i for i in arr if B > i > A])

    print(f'МАССИВ: {arr}')
    print(f'СУММА: {summ}')

    
if __name__ == '__main__':
    test2()

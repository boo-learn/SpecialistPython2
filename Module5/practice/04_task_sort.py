# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
from sort_lib import gen_list
from quick_sort import quick_sort

def test4():
    print('\nЗАДАНИЕ-4')
    arr = gen_list(20)
    print(f'МАССИВ: {arr}')
    max_arr = []

    for i in range(10):
        try:
            max_arr.append(arr.pop(arr.index(max([abs(i) for i in arr]))))
        except:
            max_arr.append(arr.pop(arr.index(max([abs(i) for i in arr])*-1)))

    summ = sum(max_arr)

    print(f'МАССИВ МАКСИМАЛЬНЫХ: {max_arr}')
    print(f'СУММА: {summ}')

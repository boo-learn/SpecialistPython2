# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
from gen_list import gen_list
from buble_sort import buble_sort

lst = gen_list(10, -5, 5)
count = 10
print(lst)

buble_sort(lst)
print(lst)
sum_i = 0
summ = 0
r_ind = len(lst)-1
l_ind = 0
while sum_i <= count:
    if lst[r_ind] >= abs(lst[l_ind]):
        summ += lst[r_ind]
        r_ind -= 1
        sum_i += 1
    else:
        summ += lst[l_ind]
        l_ind += 1
        sum_i += 1
print(summ)

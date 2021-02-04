# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
from gen_list import gen_list
from buble_sort import buble_sort

lst = gen_list(15, 0, 5)
count = 10
print(lst)
for el in range(len(lst)):
    lst[el] = -1*lst[el]
print(lst)

buble_sort(lst)
print(lst)
for el in range(len(lst)):
    lst[el] = -1*lst[el]
print(lst)

summ = 0
i = 0
while i < 10:
    summ += lst[i]
    i += 1
print(summ)

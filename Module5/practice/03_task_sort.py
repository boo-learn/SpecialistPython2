# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
from gen_list import gen_list
from bubble_sort import sort
h=gen_list(100)
sort(h)
sum=0
for i in h[-10:]:
    sum+=i
print(sum)

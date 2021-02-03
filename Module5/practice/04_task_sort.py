# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
from gen_list import gen_list
from bubble_sort import sort
h=gen_list(100)
sort(h)
sum=0
for i in h[-10:]:
    sum+=abs(i)
print(sum)

# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
from gen_list import gen_list
h=gen_list(10)
A=10
sum=0
for i in h:
    if i > A:
        sum+=i
print(sum)

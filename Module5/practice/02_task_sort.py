# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
from gen_list import gen_list
A=50
B=75
h=gen_list(100)
sum=0
for i in h:
    if B >i > A:
        sum+=i
print(sum)

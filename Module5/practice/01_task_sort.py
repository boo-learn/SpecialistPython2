from Gener_list import gen_list
from sort_bubble import sort_bubble

# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

N=20
num=gen_list(N,-20,20)
print('Исходный список: ', num)

print('Введите число: ', sep='')
a=int(input())

summa=0
count=0
for el in num:
    if el>a:
        summa+=el
        count+=1
if count!=0:
    print(f'Сумма элементов, больших {a}, равна: {summa}')
else:
    print(f'Элментов, больших {a}, нет')

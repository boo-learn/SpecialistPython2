from Gener_list import gen_list
from sort_bubble import sort_bubble

# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

N=20
num=gen_list(N,-20,20)
print('Исходный список: ', num)

print('Введите начало диапазона: ', sep='')
a=int(input())
print('Введите конец диапазона: ', sep='')
b=int(input())

summa=0
count=0
for el in num:
    if el>a and el<b:
        summa+=el
        count+=1
if count!=0:
    print(f'Сумма элементов, попадающих в диапазон [{a};{b}], равна: {summa}')
else:
    print(f'Элементов, попадающих в диапазон [{a};{b}], нет')

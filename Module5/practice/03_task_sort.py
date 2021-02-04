from Gener_list import gen_list
from sort_bubble import sort_bubble

# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов

N=20
num=gen_list(N,-20,20)
print('Исходный список: ', num)

sort_bubble(num)
print('Отсортированный список: ', num)

if N<10:
    print('В массиве меньше 10 элементов')
else:
    summa=0
    for i in range(len(num)-1,len(num)-1-10,-1):
        summa+=num[i]
    print(f'Сумма {summa}')

# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.


####
from  Lib.buble_sort import buble_sort
mass = [10,11,4 ,-5,6,-7,9,-8,7,6,5,4,-44,44,33,44,76,12,14]

i = 0
while i < len(mass)-1:
    mass[i] = abs(mass[i])
    i =i+1
print(mass)

buble_sort(mass)

print("sorted mass",mass)
i = len(mass)-1
j=0
while j<10:
    print("short",mass[i])
    j= j+1
    i= i-1

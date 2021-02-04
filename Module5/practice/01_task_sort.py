# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

from gen_list import gen_list
from bubble_sort import bubble_sort

a = 20
sum = 0
nums = gen_list(10)
bubble_sort(nums)
for i in range(len(nums)):
    if nums[i] > a:
        sum += nums[i]

print(nums)
print(sum)

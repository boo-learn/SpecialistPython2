# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов

from gen_list import gen_list
from bubble_sort import bubble_sort


nums = gen_list(3)
bubble_sort(nums)
sum = 0
if len(nums) <= 10:
    sum = sum(nums)
else:
    i = len(nums) - 10
    for i in range(len(nums)):
        sum += nums[i]

print(nums)
print(sum)

# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
from gen_list import gen_list

def get_summ(nums, threshold):
    j = len(nums)
    sum = 0
    for i in range(j):
        if nums[i] > threshold:
            sum += nums[i]
    return sum

nums = gen_list(10)
print(nums)
print(get_summ(nums, 30))

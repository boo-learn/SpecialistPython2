# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
from gen_list import gen_list

def get_summ(nums, A, B):
    if A > B:
        print("некорректные границы")
        return
    j = len(nums)
    sum = 0
    for i in range(j):
        if nums[i] > A and nums[i] < B:
            sum += nums[i]
    return sum

nums = gen_list(10)
print(nums)
print(get_summ(nums, 60, 40))

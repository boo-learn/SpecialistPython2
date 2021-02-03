# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
from gen_list import gen_list
from bubble_sort import bubble_sort


nums = gen_list(15)
print(nums)
nums1 =[]
for el in nums:
    nums1.append(abs(el))
bubble_sort(nums1)
print(nums1)
print(sum(nums1[-10:]))

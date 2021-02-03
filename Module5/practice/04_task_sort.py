# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
list1 = gen_list(20, -1, 1)
list2 = list(map(abs, list1))
sort(list2)
print(list1)
print(f"sum_max_abs = {sum(list2[-1:-11:-1])}")

# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
def conditional_sum(list, cond):
    s = 0
    for el in list:
        if el > cond:
            s += el
    return s


list1 = gen_list(10, 0, 10)

print(list1)
print(conditional_sum(list1, 1))
print(conditional_sum(list1, 5))
print(conditional_sum(list1, 10))

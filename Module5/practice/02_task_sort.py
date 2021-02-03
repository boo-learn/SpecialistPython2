# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
def conditional_sum(list, conda, condb):
    s = 0
    for el in list:
        if el > conda and el < condb:
            s += el
    return s


list1 = gen_list(10, 0, 10)

print(list1)
print(conditional_sum(list1, 1, 10))
print(conditional_sum(list1, 5, 8))
print(conditional_sum(list1, 10, 1))

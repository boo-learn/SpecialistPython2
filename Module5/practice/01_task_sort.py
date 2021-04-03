# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1

def gen_list(size, at=-100, to=100):
    import random
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))
    return data

lst = gen_list(10, 0, 30)
print('Исходный список: ', lst)

sort_lst = bubble_sort(lst)
print('Сортированный список: ', lst)

more_then = 10

lst_more_then = []

for el in lst:
    if more_then < el:
        lst_more_then.append(el)

print('Элементы бальше указанного числа', lst_more_then)

el_sum = sum(lst_more_then)

print('Сумма элементов списка', el_sum)

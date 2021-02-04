# Дан массив(список) целых чисел.
# Определить, какое число в массиве встречается чаще всего.
# Вывести это число и количество повторений.

def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]


arr = gen_list(20, at=0, to=20)
print(f'Массив {arr}')
arr_to_set = set(arr)  # Получаем множество уникальных членов массива
most_common = None
qty_most_common = 0

for item in arr_to_set:
    qty = arr.count(item)  # Получаем число вхождений значения в массиве
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item

if qty_most_common > 1:
    print(f'Чаще всего - {qty_most_common} раз(а) встречается число {most_common}')
else:
    print('Члены массива не повторяются')

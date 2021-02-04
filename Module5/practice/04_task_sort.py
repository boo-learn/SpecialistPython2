
# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.

def sort_bubble(nums):
    swapped = True
    granica = len(nums) - 1
    while swapped:
        swapped = False
        for i in range(granica):
            if abs(nums[i]) >abs(nums[i + 1]):
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        granica -= 1
    return

N=20
num=gen_list(N,-20,20)
print('Исходный список: ', num)

sort_bubble(num)
print('Отсортированный в порядке возрастания модулей: ', num)

if N<10:
    print('В массиве меньше 10 элементов')
else:
    summa=0
    for i in range(len(num)-1,len(num)-1-10,-1):
        summa+=num[i]
    print(f'Сумма {summa}')

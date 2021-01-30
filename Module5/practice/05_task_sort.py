# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
from sort_lib import gen_list

def test5():
    nums = gen_list(10)
    j = (len(nums) - 1)
    k = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(j):
            if nums[i] > nums[i + 1]:
                k += 1
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j -= 1


    print(f'МАССИВ: {nums}')
    print(f'ОБМЕНОВ: {k}')

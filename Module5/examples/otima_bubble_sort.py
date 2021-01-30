nums = [5, 2, 1, 8, 4]
swapped = True
while swapped:
    swapped = False
    j = 0
    for i in range(len(nums) - j - 1):
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            j += 1
            swapped = True
print(nums)

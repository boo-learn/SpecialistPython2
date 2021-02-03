nums = [5, 2, 1, 8, 4]
j = len(nums) - 1
swapped = True
while swapped:
    swapped = False
    for i in range(j):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
    j-=1
print(nums)

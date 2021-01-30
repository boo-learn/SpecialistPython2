nums = [5, 2, 1, 8, 4]
swapped = True

j = len(nums)

while swapped:

    swapped = False

    for i in range(j - 1):
        print("i = ",i);
#    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
    j = j - 1

print(nums)

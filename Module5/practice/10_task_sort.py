# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

from random import randint

def gen_list(count):
    arr = []
    for i in range(count):
        arr.append(randint(1, 99))
    return arr

arr = gen_list(50)
arrfirst = []
arrlast = []

print(arr)

arr.sort()

print(arr)

arr2 = arr.copy()
flag = 0

for el in arr:
    #print(el)
    arrfirst.append(el)
    arr2.remove(el)
    s1 = sum(arr2, 0)
    s2 = sum(arrfirst, 0)
    if s1/s2 <= 2 and s2 <= s1:
        print(arrfirst, " ", s2)
        print(arr2," ", s1)
        flag = 1
        break
    elif s1 != 0 and s2/s1 <= 2 and s1 <= s2:
        print(arrfirst, " ", s2)
        print(arr2," ", s1)
        flag = 1
        break
if flag == 0:
    print('Условие задачи не выполняется')

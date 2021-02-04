# Д/З
# 1.Сумма с условием
# Дан массив(список) вещественных(дробных чисел). Найдите сумму тех, которые имеют дробную часть начинающуюся с цифры 7.
# Пример: [2.123, 7.347, 5.734, 6.06, 4.72] 

print('1.Сумма с условием\n')

arr = [2.123, 7.347, 5.734, 6.06, 4.72, 45.854, 3.7 , 2.69, 12.8]
print(f'mass: {arr}')

a = 0.8
b = 0.7
s = 0

for el in arr:
    if a > el%1 >= b:
        print (el%1)
        s +=  el
        
print(f'sum: {s}')

# 2.Замена элементов
# Дан массив(список) целых чисел. Заменить все элементы массива меньше 15 их удвоенными значениями.

print('\n2.Замена элементов\n')

def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

arr = gen_list(15,1,50)

print(f'mass: {arr}')

b = 15
i = 0

for el in arr:
    if b > el:
        arr[i] = el*2
    i += 1
        
print(f'mass: {arr}')

# 3.Чаще всего
# Дан массив(список) целых чисел. Определить, какое число в массиве встречается чаще всего. Вывести это число и количество повторений

print('\n3.Чаще всего\n')

def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

arr_dig =[]
arr_fre =[]
arr = gen_list(20,1,10)

print(f'mass: {arr}')

arr.sort()

print(f'mass sort: {arr}')

i = 0
j = 0
cur = arr[0]
arr_dig.append(cur)
arr_fre.append(0)

for el in arr:
    if cur != arr[i]:
        arr_dig.append(el)
        arr_fre.append(1)
        cur = arr[i]
        j += 1
    else:
        arr_fre[j] = arr_fre[j] + 1
    i += 1
        
print(f'числа  : {arr_dig}')
print(f'частота: {arr_fre}')
print(f'макс частота: {max(arr_fre)}')
print(f'число с макс частотой повторений : {arr_dig[arr_fre.index(max(arr_fre))]}')

# 4.Анаграммы*
# Дан список слов. Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

print('\n4.Анаграммы*\n')

def letter_freq(str):

    arr = list(str)
    arr_dig =[]
    arr_fre =[]
    arr.sort()
    
    i = 0
    j = 0
    cur = arr[0]
    arr_dig.append(cur)
    arr_fre.append(0)

    for el in arr:
        if cur != arr[i]:
            arr_dig.append(el)
            arr_fre.append(1)
            cur = arr[i]
            j += 1
        else:
            arr_fre[j] = arr_fre[j] + 1
        i += 1

    return [arr_dig,arr_fre]

spisok = ['мука','кума','насос','кабан','слово','умка','нитка','ель','эль','молоко','лунь','сокол','нуль','сосна','банка','ткани']
print(f'слова: {spisok}')

i =0 
j = 0
first = False
outlst = []

for el in spisok:
    j = 0
    first = True
    for el2 in spisok:
        if i != j and letter_freq(el) == letter_freq(el2):
                outlst.append(el2)
                spisok.remove(el2)
                if first:
                    outlst.append(el)
                    spisok.remove(el)
                    first = False
        j += 1

    i += 1
    
print('анаграммы:',outlst)

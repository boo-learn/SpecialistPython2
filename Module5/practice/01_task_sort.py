# Домашнее задание 4
# Анаграммы.
# Дан список слов. Найти в нем все анаграммы
# (слова, составленные из одних и тех же букв).

arr = ['кот', 'Ток', 'палка', 'Лапка', 'снег', 'нега']

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    return (str1_list == str2_list)
    
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if isAnagram(arr[i].lower(), arr[j].lower()):
            print(f'{arr[i]} и {arr[j]} - анаграммы')
            

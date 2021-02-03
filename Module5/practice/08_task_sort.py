# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
from bubble_sort import sort
new_list=[]
new_phones=[]
for i in phones:
    new_list.append(i.split("-"))
# new_list.sort()
sort(new_list)
for i in new_list:
    new_phones.append('-'.join(i))
print(new_phones)

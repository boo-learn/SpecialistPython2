# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
from gen_list import gen_list
from bubble_sort import sort
h=gen_list(100)
print(h)
j=sort(h)
print(j)
print(h)

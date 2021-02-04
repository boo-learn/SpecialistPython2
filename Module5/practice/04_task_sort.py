# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
from gen_list import gen_list
from bubble_sort import sort
h=gen_list(100)
sort(h)
print(h)
sum=0
new_list=[]
for i in h:
    new_list.append(abs(i))
sort(new_list)
temp1=new_list[-10:]
for i in temp1:
    sum+=i
print(sum)

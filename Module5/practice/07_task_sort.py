# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
goods = [5,2,1,10,50,10,4]

goods1 = sorted(goods)
goods2 = sorted(goods,reverse=True)

print(goods2)
print(goods1[0:len(goods)//2])

goods3 = goods1[0:len(goods)//2]


lall = len(goods2)
lfree= len(goods1[0:len(goods)//2])

print(  goods2[0:lall - lfree])

res = []
for i in range(0,lall - lfree):
    res.append(goods2[i])
    if i < lfree:
        res.append(goods3[i])

print(res)
print(sum(goods2[0:lall - lfree]))

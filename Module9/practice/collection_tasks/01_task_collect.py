# Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров —
# от шифра Цезаря до шифровальной машины «Энигма».
# Выполним простой частотный анализ: выясним, какой символ чаще всего
# встречается в данном тексте.

import collections


text = 'jhsygbxikujshdd ujhbisedcewfkjkjhkhndcolidjsci dc hduh udh cuod h'
counter = collections.Counter(text)
print(counter.most_common())

i = 0
print(f"символ {counter.most_common()[i][0]} чаще всех встречается")
while counter.most_common()[i+1][1] == counter.most_common()[i][1]:
    print(f"символ {counter.most_common()[i+1][0]} чаще всех встречается")
    i += 1

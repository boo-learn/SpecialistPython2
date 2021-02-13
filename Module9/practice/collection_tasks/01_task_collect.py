# Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров —
# от шифра Цезаря до шифровальной машины «Энигма».
# Выполним простой частотный анализ: выясним, какой символ чаще всего
# встречается в данном тексте.

# Входные данные:
# Произвольный текст
# TODO: your code here...

import collections

# collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов
counter = collections.Counter()


text = ''' Этоважнейшийинструментвзломамногих классических шифров —
от шифраЦезарядошифровальноймашины«Энигма».
Выполним простой частотныйанализ:выясним, какой символ чаще всего
встречается в данном тексте.
'''
for char in text:
    counter[char] += 1

print("символ чаще всего встречается в данном тексте: ", counter.most_common(1)[0][0])

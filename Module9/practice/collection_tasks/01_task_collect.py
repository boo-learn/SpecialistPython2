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
txt = []
text = ("There has been a few other similar improvements in the latest release ... but this one example should suffice to illustrate the work done to make Python even friendlier to beginners.  However, this is unfortunately not the whole story.")
text = text.replace(' ', '')
for x in text:
    txt.append(x)
#text = text.split(' ')

for x in txt:
    counter[x] += 1

print(counter)

# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

from pprint import pprint

words = ["not_an_anagram", "anagram", "something_1", "garmaan", "python", "pascal", "tyhonP"]
unique_words_sl = set(["".join(sorted(w)) for w in words])
angm_lsts = []
first = True
for word in words:
    if first:
        angm_lsts.append([word])
        first = False
        print("first added")
        continue
    found = False
    for al in angm_lsts:
        for a in al:
            if "".join(sorted(word.lower())) == "".join(sorted(a.lower())):
                print("found")
                al.append(word)
                found = True
                break
        if found: break
    if not found:
        angm_lsts.append([word,])

for l in angm_lsts:
    if len(l) > 1:
        pprint(l)

# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
ef is_anagram(st,st1):
    if len(st1)!=len(st) or (st)==st1=="":
        return False
    st=st.lower()
    st1=st1.lower()
    dict1={}
    dict2={}
    for i in st:
        dict1.update({i:st.count(i)})
    for i in st1:
        dict2.update({i:st1.count(i)})
    return dict1==dict2

def analiz_anagram (slova):
    dict_a={}
    for i in range(0,len(slova)-1):
        anagrams = []
        #print(f"i=={i}")
        for j in range(i+1,len(slova)):
            #print(f"j == {j}")
            if is_anagram(slova[i],slova[j]):
                print(f" i= {i} {slova[i]} j= {j}  {slova[j]}")
                print(slova[j])
                #anagrams.append(slova.pop(j)) #здесь ошибка
                #j -= 1
                print(f" i= {i} {slova[i]} j= {j}  {slova[j-1]}")
                #j-=1
                anagrams.append(slova[j])
                slova[j]=''

        if len(anagrams)>0:
            dict_a.update({slova[i]:anagrams})
            print(dict_a)
            #print(b)
    return dict_a



slova=['sfrea','dfrwc','safre','abba','baba','aabb','aabb','dopel','Dolep','dse','dkhky','bbaa']

#print(is_anagram(slova[0],slova[2]))

dict=analiz_anagram(slova)
print (dict)
print (slova)

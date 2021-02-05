# задание по поиску наиболее часто встречающегося числа из списка
def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]


def frex_dict(mas):
    dict = {}
    for di in d:
        dict.update({di: d.count(di)})
    return dict

def max_frex(dict):
    max_dict={}
    for i in list(dict.keys()):
        if dict.get(i) == max(list(dict.values())):
            max_dict.update({i:dict.get(i)})
    return max_dict

#d = [1, 2, 4, 5, 2, 5, 1, 4, 1, 3, 2, 3]
d=gen_list(100,-5,5)
frex_d= frex_dict(d)
#print(d)
#print(frex_d)
print (max_frex(frex_d))

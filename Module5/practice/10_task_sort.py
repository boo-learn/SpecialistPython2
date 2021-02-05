#  замена в списке элемента его удвоением
def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

def replace_double(mas,value):
    for i in range(0,len(mas)):
        if mas[i]<value:
            mas[i]=mas[i]*2
    return mas

mas1=gen_list(10,1,30)
print(mas1)
print(replace_double(mas1,15))

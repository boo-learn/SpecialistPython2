# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

def two_hills (stones):
    stones.sort(reverse=True)
    if stones[0]>sum(stones[1:])*2 or len(stones)<2:
        return False
    hill1=[]
    hill2=[]

    for i in range (0, len(stones),2):
        hill1.append(stones[i])
        stones[i]=0
        if stones[i + 1] > sum(stones[i + 2:]):
            for j in range (i+1, len(stones)):
                hill2.append(stones[j])

            return hill1,hill2
        hill2.append(stones[i+1])
    return hill1, hill2

stones=[100,10,3,5,2,3]
#stones=gen_list(10,1,30)
print(stones)
rez=two_hills(stones)
if rez != False:
    print (f" {rez[0]}  {sum(rez[0])} {rez[1]} {sum(rez[1])} ")
else:
    print ('Невозможно')

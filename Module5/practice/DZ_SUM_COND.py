# 
# Сумма с условием
# Дан массив(список) вещественных(дробных чисел). Найдите сумму тех,
# которые имеют дробную часть начинающуюся с цифры 7.
# Пример: [2.123, 7.347, 5.734, 6.06, 4.72]

def gen_list_float(size, max_abs=100):
    '''
    create a list of non-negative floating point numbers   
    '''
    import random
    return [round(random.random() * max_abs, 6) for _ in range(size)]


def sum_sum_fract_part(list_float, fract_part=7):
    '''
    Find the sum of those that have a fractional part
    starting with a number <fract_part>
    '''
    # create a copy of the list so as not to modify it   
    copy_list = list_float.copy()
    copy_list.sort(key=lambda el: int(abs(el) * 10 % 10))
    sum_ft = 0
    for el in copy_list:
        fract_part_curr = int(abs(el)* 10 % 10)
        if fract_part_curr > fract_part:
            break
        if fract_part_curr == fract_part:
            sum_ft += el
    return sum_ft

def main():
    
    mass1 = gen_list_float(20, max_abs=10)
    print(mass1)
    print(sum_sum_fract_part(mass1, fract_part=7))

    mass2 = gen_list_float(20, max_abs=10)
    print(mass2)
    print(sum_sum_fract_part(mass2, fract_part=4))
    # 
    mass3 = [-2.123, 7.347, -5.734, 6.06, 4.72]
    print(mass3)
    print(sum_sum_fract_part(mass3, fract_part=7))



if __name__=='__main__':
    main()

# Анаграммы*
# Дан список слов. Найти в нем все анаграммы
# (слова, составленные из одних и тех же букв).

def is_anagrams(str1, str2):
    lst_str1 = list(str1)
    lst_str2 = list(str2)
    lst_str1.sort()
    lst_str2.sort()
    return lst_str1 == lst_str2

def all_anagrams(list_words):
    #  создаем список для списков анаграмм
    list_anagrams = []
    #  копируем список для работы с ним
    copy_list_words = list_words.copy()
    #  отсортируем по длине слова
    copy_list_words.sort(key=lambda el: len(el))
    #  берем первое слово и сравниваем с другими
    while len(copy_list_words):  #  пока список не пустой
        #  создаем список анаграмм   
        list_anagr = [copy_list_words[0]]
        count_anagr = 1
        #   
        for j in range(1, len(copy_list_words)):
            if len(copy_list_words[j]) > len(copy_list_words[0]):
                #  если длина слова больше длины первого в списке
                #  нет смысла искать анаграммы для них и последующих слов
                break
            if is_anagrams(copy_list_words[0], copy_list_words[j]):
                #  если являются анаграммами
                list_anagr.append(copy_list_words[j])
                count_anagr += 1
        
        #  удаляем из списка слова, которые мы уже выделили
        #  как анаграммы для первого слова
        for word_for_del in list_anagr:
            copy_list_words.remove(word_for_del)

        #  если в списке есть не только первое слово,
        #  то добавляем в список для списков анаграмм
        if count_anagr > 1:
            list_anagrams.append(list_anagr)
                       
    return list_anagrams

def print_all_anagrams(list_anagrams):
    '''
      print lists anagrams
    '''
    if len(list_anagrams):
        print('lists anagrams:')
        for i, anagr in enumerate(list_anagrams):
            print(i + 1, '-', *anagr)
    else:
        print('no anagrams')
        

def main():
    
    mass1 = ['qwe','4','3','rrrrrr','er','rr','zdf']
    
    print(mass1)
    print_all_anagrams(all_anagrams(mass1))
    
    mass2 = ['mama','amam','petr','ananas','maam','nanasa','zdf','ananas']
    
    print(mass2)
    print_all_anagrams(all_anagrams(mass2))
    
    mass3 = ['mama','amam','petr','ananas','maam','nanasa','zdf', \
              'papa','papa','q','q','rt','tr','zdf' \
              'qwerty','ytrewq','qwe','ananas2','maam2','nanasa2','zdfqwweerr']
    
    print(mass3)
#    print('list anagrams', all_anagrams(mass3))
    print_all_anagrams(all_anagrams(mass3))


if __name__=='__main__':
    main()


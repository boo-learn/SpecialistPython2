class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.__len = 0
        self.__mem = None

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ''
            while current.next is not None:
                current = current.next
                out += ','+str(current.value)
            return out + ']'
        return 'LinkedList []'



    def clear(self):
        self.first=None
        self.last = None
        self.__len=0
        #raise TypeError("Not implemented")

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        # Создаем новый узел
        new_node = Node(value, None)
        if self.first is None:
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = new_node
        else:
            # здесь, уже на разные
            new_node = Node(value, None)
            self.last.next = new_node
            self.last = new_node
        self.__len +=1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node
        self.__len += 1

    def cut (self):
        """
        Удаляет последний элемент в списке
        """
        if self.first is None or self.last is None:
            return None
        if self.first==self.last:
            self.first = None
            self.last = None
            self.__len -= 1
            return None
        current=self.first
        current1=current.next
        while current1.next is not None:
            current=current.next
            current1=current1.next
        self.last = current
        current.next=None
        self.__len -= 1


        self.__len -= 1
        #print (self.__len )

    def insert(self, value, index):
        if index>= self.len():
            self.add(value)
            return
        if index==0:
            self.push(value)
            return
        current=self.first
        current_index=0
        up=None
        while True :
            if current_index == index-1:
                up = current
                break
            current = current.next
            current_index+=1
        self.__len += 1


        new_node=Node(value,up.next)
        up.next=new_node


        """
        Вставляет узел со значением value на позицию index
        """
        # TODO: реализовать вставку
        #raise TypeError("Not implemented")

    def find(self, value):
        if self.first is None:
            return None, None
        current = self.first
        current_index=0
        while current.next is not None:
           if current.value == value:
              return current_index, current.value
           current_index+=1
           current=current.next
        return None, value

        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        #raise TypeError("Not implemented")

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        #length = 0
        #if self.first is not None:
        #    current = self.first
        #    while current.next is not None:
        #        current = current.next
        #       length += 1
        #return length + 1  # +1 для учета self.first
        return self.__len

    def __iter__(self):
        self.__mem=self.first
        return self

    def __next__(self):
        if self.__mem is None:
            raise StopIteration
        value=self.__mem.value
        self.__mem=self.__mem.next
        return value

    def reverse(self):
        L1=LinkedList()
        while self.first is not None:
            L1.add(self.last.value)
            self.cut()

        return (L1)





if __name__ == "__main__":
    L = LinkedList()
    
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(5)
    L.add(9)
    L.add(10)
    L.add(11)

    print(L)
   # L.clear()
    L.insert(16,3)
    print(L)
    val=10
    print(f"find at index {L.find(val)[0]} value = {L.find(val)[1]}")
    L.cut()
    print(L)
    print(L.len())
    L1=L.reverse()
    print(L1)


    # TODO: реализовать интерфейс итерации
    # for el in L:
    #     print(el)
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    # TODO: реализовать обращение по индексу и изменение значение по индексу
    # print(L[0])
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    # L = LinkedList(2, 4, 6, -12)
    # print(L)

    # TODO: реализовать интерфейс итерации
    # for el in L:
    #     print(el)
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    # TODO: реализовать обращение по индексу и изменение значение по индексу
    # print(L[0])
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    # L = LinkedList(2, 4, 6, -12)
    # print(L)

class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    # def __repr__(self):
    #     return f"{self.value} -> {self.next}"


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.__length = 0

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента ##DONE
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value)
                if current.next is not None:
                    out += ','
            return out + ']'
        return 'LinkedList []'
    
    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка #done
        # raise TypeError("Not implemented")
        self.first = None
        self.last = None

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
        self.__length += 1

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
        self.__length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        # TODO: #done реализовать вставку


        new = Node(value)  # next is empty yet
        if index == 0:
            self.push(value)
            return
        if index == self.__length:
            self.add(value)
            return
        if index > self.__length:
            self.add(value)
            return

        curr: Node = self.first
        for i in range(index-1):
            curr = curr.next
        new.next = curr.next  # now new point to list[index+1]
        curr.next = new

        self.__length += 1

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        raise TypeError("Not implemented")

    def len(self):
        # TODO: #done сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        """length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first"""
        return self.__length


if __name__ == "__main__":
    L = LinkedList()
    L.add(1)
    L.add(2)
    L.add(3)
    print(L)
    L.insert(4, 0)
    print(L)
    L.insert(5, 4)
    print(L)
    L.insert(5, 8)
    print(L.len())

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

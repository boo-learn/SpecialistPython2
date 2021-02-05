class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node: {self.value} --> {self.next}"


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.__len = 0
        self.__next = None
        for arg in args:
            self.add(arg)

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            return out.strip(',') + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self.__init__()

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
        self.__len += 1

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

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if self.first is None or index == 0:
            self.push(value)
            return

        if index >= self.len():
            self.add(value)
            return

        index_prev = 0
        current = self.first
        prev = current
        while True:
            if index == index_prev + 1:
                prev = current
                break
            current = current.next
            index_prev += 1

        new_node = Node(value, prev.next)
        prev.next = new_node
        self.__len += 1


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
        return self.__len

    def __iter__(self):
        self.__next = self.first
        return self

    def __next__(self):
        if self.__next.next is None:
            raise StopIteration
        value = self.__next.value
        self.__next = self.__next.next
        return value

    def __getitem__(self, index):
        if isinstance(index, slice):
            # index.start
            # index.stop
            # index.step
            return

        if index < 0:
            index = self.len() + index

        if index >= self.len() or index < 0:
            raise IndexError("Index out of range")

        current = self.first

        for _ in range(index):
            current = current.next

        return current.value


if __name__ == "__main__":
    # L = LinkedList()
    # L.add(1)
    # L.add(2)
    # L.add(3)
    #
    # print(L[0])
    # print(L[1])
    # print(L[2])

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
    # L.__getitem__(0)
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    L = LinkedList(2, 4, 6, -12)
    print(L[0])
    print(L[1])
    print(L[2])
    print(L[3])
    L1 = LinkedList(3)
    L1.add(77)
    print(L1)

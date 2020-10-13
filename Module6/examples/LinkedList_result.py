class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.__current_iter = None
        for el in args:
            self.add(el)

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ',' + str(current.value)
            return out + ']'
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
            self.last.next = new_node
            self.last = new_node

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

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index == 0:
            self.push(value)
            return
        if index >= self.len():
            self.add(value)
            return
        current = self.first
        current_index = 0
        while current_index != index - 1:
            current = current.next
            current_index += 1
        prev = current
        next = current.next
        new_node = Node(value, next)
        prev.next = new_node

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        current = self.first
        index = 0
        try:
            while current.value != value:
                current = current.next
                index += 1
        except AttributeError:
            raise ValueError(f"{value} is not in LinkedList")
        return index

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first

    def __next__(self):
        if self.__current_iter is None:
            raise StopIteration
        value = self.__current_iter.value
        self.__current_iter = self.__current_iter.next
        return value

    def __iter__(self):
        self.__current_iter = self.first
        return self

    def __getitem__(self, index):
        # TODO: убрать дублирование кода
        if index > self.len() - 1:
            raise IndexError("LinkedList index out of range")
        current = self.first
        current_index = 0
        while current_index != index:
            current = current.next
            current_index += 1

        return current.value

    def __setitem__(self, index, new_value):
        if index > self.len() - 1:
            raise IndexError("LinkedList index out of range")
        current = self.first
        current_index = 0
        while current_index != index:
            current = current.next
            current_index += 1

        current.value = new_value

if __name__ == "__main__":
    # L = LinkedList()
    # L.add(1)
    # L.add(2)
    # L.add(3)
    # L.insert(-4, 1)
    # print(L)

    # print(L.find(45))

    # for el in L:
    #     print(el)

    # print(L[5])
    # L[10] = "new"
    # print(L[1])
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    # print(L[0]) L.__getitem__(0)
    # L[0] = "new" L.__setitem__(0, "new")
    # print(L[0])

    L = LinkedList()
    print(L)

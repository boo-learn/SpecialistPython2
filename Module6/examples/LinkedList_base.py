# Для Связанного списка(LinkedList) реализуйте метод reverse() - меняющий значения
# всех нод(узлов) на противоположное. Значение первой ноды становится
# значением последней, значение второй, значением предпоследней.
# Примечание: при реализации не используйте список(list).


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

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            # << FIXME    
            else:
                out = out[:len(out)-1]
            # FIXME >>        
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        raise TypeError("Not implemented")

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
        if index >= self.len():
            self.add(value)
            return
        if index == 0:
            self.push(value)
            return

        current = self.first
        current_index = 0
        node_up = None
        while True:
            if current_index == index - 1:
                node_up = current
                break
            current = current.next
            current_index += 1

        new_node = Node(value, node_up.next)
        node_up.next = new_node
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
    
    def change_value_by_index(self, index):
        """
        меняем значения соседних узлов с индексами index и index + 1
        """
        if self.__len < 2:
            return
        
        if index >= self.__len - 1:
            # индекс последнего символа или вне списка
            return
              
        current = self.first
        current_index = 0
        while True:
            if current_index == index:
                current.value, current.next.value = current.next.value, current.value
                break
            current = current.next
            current_index += 1
            
    
    def reverse(self):
        """
        меняет значения
        всех нод(узлов) на противоположное. Значение первой ноды становится
        значением последней, значение второй, значением предпоследней.
        """
        if self.__len < 2:
            return
        
        for i in range(self.__len - 1):
            for j in range(self.__len - 1 - i):
                self.change_value_by_index(j)

    def len(self):
        return self.__len


if __name__ == "__main__":
    L = LinkedList()
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(4)
    L.add(5)
    L.add(6)
    print(L)
    L.change_value_by_index(8)
    print(L)
# 
#  #   print(L)
#     L.insert(10, 0)
    # print(L)
    L.reverse()
    print(L)


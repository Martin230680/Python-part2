from typing import Any, Optional

class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Node[{value}]'.format(value=str(self.value))

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList[]'

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            self.length += 1  # Увеличиваем длину списка
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index: int) -> None:
        if index < 0 or index >= self.length:
            raise IndexError('Индекс за пределами списка')
        cur_node = self.head
        if index == 0:
            self.head = cur_node.next
            self.length -= 1
            return
        prev = None
        for _ in range(index):
            prev = cur_node
            cur_node = cur_node.next
        prev.next = cur_node.next
        self.length -= 1

    def get(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            raise IndexError('Индекс за пределами списка')
        t_node = self.head
        for _ in range(index):
            t_node = t_node.next
        return t_node.value

# Пример использования
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(2)
print('Новый список:', my_list)


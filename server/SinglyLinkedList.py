class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.length: int = 0

    def is_empty(self) -> bool:
        return self.head == None

    # agrega un elemento al principio de la lista
    def add_first(self, value: int):
        new_nodo: Node = Node(value)
        if self.is_empty():
            self.head = new_nodo
        else:
            new_nodo.next = self.head
            self.head = new_nodo

        self.length += 1

    def linked_list_to_list(self) -> list:
        the_list = []

        if self.length > 0:
            aux: Node = self.head

            while aux != None:
                the_list.append(aux.data)
                aux = aux.next

            return the_list
        return the_list

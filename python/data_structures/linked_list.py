class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def add_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        return False

    def __str__(self):
        if self.head is None:
            return "NULL"

        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next_node

        values.append("NULL")
        return " -> ".join(values)


class TargetError:
    pass

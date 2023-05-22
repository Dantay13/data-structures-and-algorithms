class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def insert(self, value):
        # method body here
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        # method body here
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        # method body here
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(['{ ' + value + ' }' for value in values] + ['NULL'])


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


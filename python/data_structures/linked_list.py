class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    """
    Put docstring here
    """

    class Node:

        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self):
        # initialization here
        self.head = None

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


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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, target_value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise TargetError("Empty list: Cannot insert before.")
        elif self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.next.value == target_value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            raise TargetError("Target value not found: Cannot insert before.")

    def insert_after(self, target_value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise TargetError("Empty list: Cannot insert after.")
        current = self.head
        while current:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise TargetError("Target value not found: Cannot insert after.")

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


class TargetError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, value):
        # method body here
        new_node = Node(value)
        if self.back is None:
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        self.size -= 1
        return value

    def peek(self):
        if self.front is None:
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        current_node = self.head
        output = ""
        while current_node:
            output += "{ " + str(current_node.data) + " } -> "
            current_node = current_node.next
        output += "NULL"
        return output

from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        # Move all elements from stack1 to stack2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        # Push the new value to stack1
        self.stack1.push(value)
        # Move all elements back from stack2 to stack1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        # Remove and return the top element from stack1
        return self.stack1.pop()

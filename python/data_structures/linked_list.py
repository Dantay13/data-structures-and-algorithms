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

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        if not self.head:
            return "NONE"

        output = ""
        current = self.head
        while current:
            output += f"{{ {current.value} }} -> "
            current = current.next_node
        output += "NONE"
        return output

    def some_method(self):
        # method body here
        pass


class TargetError:
    pass

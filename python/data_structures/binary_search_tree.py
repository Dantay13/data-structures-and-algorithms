from data_structures.binary_tree import BinaryTree, Node

class Node:
    """
    this is a node class, which represent a binary node with two children but they are empty
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(BinaryTree):
    """
    This is a binary search tree, which is a non-linear data structure, that takes in a node with value and a left and right child. In the BTS the left child has a lesser value than the parent node, and the right child has a higher value that the parent child
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def add(self, value):
        # method body here
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(value, self.root)

    def _insert_recursively(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(value, node.right)

    def contains(self, value):
        return self._search_recursively(value, self.root)

    def _search_recursively(self, value, node):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursively(value, node.left)
        else:
            return self._search_recursively(value, node.right)


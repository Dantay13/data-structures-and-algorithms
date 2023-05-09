from data_structures.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    This is a binary search tree, which is a non-linear data structure, that takes in a node with value and a left and right child. In the BTS the left child has a lesser value than the parent node, and the right child has a higher value that the parent child
    """

    def __init__(self, value, left=None, right=None):
        # initialization here
        self.value = value
        self.left = left
        self.right = right

    def some_method(self):
        # method body here
        pass

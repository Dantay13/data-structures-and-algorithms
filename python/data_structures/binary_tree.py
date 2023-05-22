class BinaryTree:
    """
    This is a binary tree, which is a non-linear data structure, that takes in a node with value and a left and right child. Binary meaning two child node;.
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def pre_order(self): # pre-order traversal is node/root, left node,  right node
        traversal = []

        def insert(root): # helper function
            if root:
                # root
                traversal.append(root.value) # operation on the root/node
                # left
                insert(root.left)
                #right
                insert(root.right)

        # remember to invoke the helper function
        insert(self.root)

        return traversal

    def in_order(self):
        traversal = []

        def insert(root):
            if root:
                insert(root.left)
                traversal.append(root.value)
                insert(root.right)

        insert(self.root)

        return traversal

    def post_order(self):
        traversal = []

        def insert(root):
            if root:
                insert(root.left)
                insert(root.right)
                traversal.append(root.value)

        insert(self.root)

        return traversal

    def contains(self, value):
        return self._search_recursively(value, self.root)

    def _search_recursively(self, value, node):
        if node is None:
            return False
        if node.value == value:
            return True
        return self._search_recursively(value, node.left) or self._search_recursively(value, node.right)

    def find_maximum_value(self):
        return self._find_maximum_value_recursively(self.root)

    def _find_maximum_value_recursively(self, node):
        if node is None:
            return float('-inf') # Return negative infinity for an empty tree

        max_value = node.value
        left_max = self._find_maximum_value_recursively(node.left)
        right_max = self._find_maximum_value_recursively(node.right)

        max_value = max(max_value, left_max, right_max)
        return max_value

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


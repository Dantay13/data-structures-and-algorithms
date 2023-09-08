from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    hashmap = Hashtable()
    common_values = set()

    pre_order_traversal(tree1, hashmap)

    def check_common(root):
        nonlocal common_values
        if root is None:
            return
        if hashmap.contains(root.value):
            common_values.add(root.value)
        check_common(root.left)
        check_common(root.right)

    check_common(tree2)

    return common_values

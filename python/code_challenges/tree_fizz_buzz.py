from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
import copy


def fizz_buzz_tree(tree):
    def traverse_tree(node):
        if node is None:
            return

        new_node = copy.deepcopy(node)  # Create a new node with the same value
        if new_node.value % 3 == 0 and new_node.value % 5 == 0:
            new_node.value = "FizzBuzz"
        elif new_node.value % 3 == 0:
            new_node.value = "Fizz"
        elif new_node.value % 5 == 0:
            new_node.value = "Buzz"
        else:
            new_node.value = str(new_node.value)

        new_node.children = [traverse_tree(child) for child in new_node.children]
        return new_node

    new_tree = KaryTree(traverse_tree(tree.root))
    return new_tree



import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

"""
added tests
"""

def test_max_val_empty_tree():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = float('-inf')
    assert actual == expected

def test_max_val_one_node():
    tree = BinaryTree()
    tree.root = Node(5)
    actual = tree.find_maximum_value()
    expected = 5
    assert actual == expected

def test_max_val_negative_values():
    tree = BinaryTree()
    tree.root = Node(-10)
    tree.root.left = Node(-30)
    tree.root.right = Node(-7)
    actual = tree.find_maximum_value()
    expected = -7
    assert actual == expected

def test_max_val_large_tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(30)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(50)
    tree.root.right.left = Node(60)
    tree.root.right.right = Node(70)
    actual = tree.find_maximum_value()
    expected = 70
    assert actual == expected

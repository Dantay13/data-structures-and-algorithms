import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


def test_contains(tree):
    actual = tree.contains("a")
    expected = True
    assert actual == expected

def test_contains_deeper(tree):
    actual = tree.contains("c")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_not_contains(tree):
    actual = tree.contains(100)
    expected = False
    assert actual == expected


def test_max_value(tree):
    actual = tree.find_maximum_value()
    expected = 7
    assert actual == expected


def test_find_maximum_value_empty_tree():
    empty_tree = BinaryTree()
    actual = empty_tree.find_maximum_value()
    expected = float('-inf')
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")


    return tree

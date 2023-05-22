import pytest
from data_structures.linked_list import LinkedList, TargetError


# @pytest.mark.skip("TODO")
def test_kth_from_end_zero():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_one():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_two():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_out_of_range():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(3)


# @pytest.mark.skip("TODO")
def test_kth_from_end_under_range():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(-1)


# @pytest.mark.skip("TODO")
def test_kth_from_end_size_one():
    linked_list = LinkedList()
    linked_list.insert("apples")
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected

"""
additional tests
"""

def test_kth_from_end_large_k():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers"]
    for value in reversed(values):
        linked_list.insert(value)
    with pytest.raises(TargetError):
        linked_list.kth_from_end(10)

def test_kth_from_end_middle():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers", "dates"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(2)
    expected = "bananas"
    assert actual == expected

def test_kth_from_end_last():
    linked_list = LinkedList()
    values = ["apples", "bananas", "cucumbers", "dates"]
    for value in reversed(values):
        linked_list.insert(value)
    actual = linked_list.kth_from_end(3)
    expected = "apples"
    assert actual == expected

def test_kth_from_end_empty_list():
    linked_list = LinkedList()
    with pytest.raises(TargetError):
        linked_list.kth_from_end(0)

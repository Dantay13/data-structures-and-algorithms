import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected

def test_set_value():
    hashtable = Hashtable(1024)
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")

    assert hashtable.get("key1") == "value1"
    assert hashtable.get("key2") == "value2"

def test_retrieve_nonexistent_key():
    hashtable = Hashtable(1024)
    assert hashtable.get("nonexistent_key") is None

def test_get_unique_keys():
    hashtable = Hashtable(1024)
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    hashtable.set("key3", "value3")

    assert sorted(hashtable.keys()) == ["key1", "key2", "key3"]

def test_collision_handling():
    hashtable = Hashtable(1024)
    # Set two keys that collide
    hashtable.set("abc", "value1")
    hashtable.set("acb", "value2")

    assert hashtable.get("abc") == "value1"
    assert hashtable.get("acb") == "value2"

def test_retrieve_value_from_collision_bucket():
    hashtable = Hashtable(1024)
    # Set two keys that collide
    hashtable.set("abc", "value1")
    hashtable.set("acb", "value2")

    # Ensure retrieving values from the same bucket works
    assert hashtable.get("abc") == "value1"
    assert hashtable.get("acb") == "value2"

def test_hash_key_within_range():
    hashtable = Hashtable(1024)
    key = "test_key"
    hashed_index = hashtable.hash(key)

    assert 0 <= hashed_index < 1024


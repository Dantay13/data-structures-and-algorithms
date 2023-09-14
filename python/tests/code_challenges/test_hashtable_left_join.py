import pytest
from code_challenges.hashtable_left_join import left_join

def test_exists():
    assert left_join

def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_no_antonyms():
    # Test when there are no antonyms, only synonyms
    synonyms = {
        "happy": "joyful",
        "hot": "scorching",
        "good": "excellent",
    }
    antonyms = {}

    expected = [
        ["happy", "joyful", "NONE"],
        ["hot", "scorching", "NONE"],
        ["good", "excellent", "NONE"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_empty_input():
    # Test when both synonym and antonym dictionaries are empty
    synonyms = {}
    antonyms = {}

    expected = []

    actual = left_join(synonyms, antonyms)

    assert actual == expected



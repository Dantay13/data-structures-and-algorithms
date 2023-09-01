from data_structures.hashtable import Hashtable


def first_repeated_word(s):
    word_map = Hashtable()
    words = s.split()

    for word in words:
        word = word.lower().strip(',.!?')
        if word_map.contains(word):
            return word
        else:
            word_map.add(word, True)

    return None



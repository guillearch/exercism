from collections import Counter


def find_anagrams(word, candidates):
    return [i for i in candidates
            if Counter(word.lower()) == Counter(i.lower())
            and word.lower() != i.lower()]

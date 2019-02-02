import re
from collections import Counter


def word_count(phrase):
    words = re.findall(r'[a-z0-9]+(?:\'[tsmldvr])?', phrase.lower())
    return dict(Counter(words))

import re
from collections import Counter

p = re.compile(r'[a-z0-9]+(?:\'[tsmldvr])?')


def word_count(phrase):
    words = p.findall(phrase.lower())
    return Counter(words)

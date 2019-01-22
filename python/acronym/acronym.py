import re

def abbreviate(words):
    words = re.sub(r'[^\w\s\-]', '', words)
    return ''.join([letter for letter in words.title() if letter.isupper()])

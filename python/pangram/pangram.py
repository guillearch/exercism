def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in sentence.lower():
            return False
    return True

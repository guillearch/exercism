import random
import string

class Robot(object):

    names = []

    def __init__(self):
        self.reset()

    def generate_name(self):
        while True:
            name = self.random_string()
            if name not in self.names:
                return name

    def random_string(self):
        return ''.join(random.choice(string.ascii_uppercase)
                       for _ in range(2)) + \
                ''.join(random.choice(string.digits)
                        for _ in range(3))

    def reset(self):
        self.name = self.generate_name()
        self.names = [self.name]

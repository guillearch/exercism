import random
import math

class Character:

    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def roll_dice(self):
        return [random.randint(1,6) for i in range (4)]

    def discard(self, results):
        return results.remove(min(results))

    def ability(self):
        results = self.roll_dice()
        self.discard(results)
        return sum(results)

def modifier(value):
    return math.floor((value-10)/2)

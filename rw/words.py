"""
this module chooses all the appropriate words for you
"""

import random

monsters = [
    {"s": "Dalek", "p": "Daleks"},
    {"s": "Cyberman", "p": "Cybermen"},
    {"s": "Sea Devil", "p": "Sea Devils"},
    {"s": "Angel", "p": "Angels"},
    {"s": "Silurian", "p": "Silurians"},
    {"s": "Rutan", "p": "Rutans"},
    {"s": "Bandrill", "p": "Bandrills"},
    {"s": "Vashta Nerada", "p": "Vashta Nerada"},
    {"s": "Dinosaur", "p": "Dinosaurs"},
    {"s": "Planet", "p": "Planets"},
    {"s": "Doctor", "p": "Doctors"},
    {"s": "Chumbly", "p": "Chumblies"},
    {"s": "Terileptil", "p": "Terileptils"},
    {"s": "Judoon", "p": "Judoon"},
    {"s": "Zygon", "p": "Zygons"},
    {"s": "Morbius", "p": "Time Lords"},
    {"s": "Omega", "p": "CIA"},
    {"s": "Axon", "p": "Axons"},
    {"s": "Wirrn", "p": "Wirrn"},
    {"s": "Ice Warrior", "p": "Ice Warriors"},
    {"s": "Yeti", "p": "Yeti"},
    {"s": "Auton", "p": "Autons"},
]

monsters += [{"s": "Dalek", "p": "Daleks"}] * 6
monsters += [{"s": "Cyberman", "p": "Cybermen"}] * 5
monsters += [{"s": "Master", "p": "Master"}] * 4
monsters += [{"s": "Sontaran", "p": "Sontarans"}] * 3


class Monster:
    """
    simple class for monster building
    """
    def __init__(self):
        """
        on init create the monster
        """
        self.singular = ""
        self.plural = ""
        self.populate()

    def populate(self):
        """
        chooses a monster then populates
        the singular and plural
        """
        monster = random.choice(monsters)
        self.singular = monster["s"]
        self.plural = monster["p"]

    def incorrect(self):
        """
        if we don't like it, give us another one
        """
        self.populate()

def get_word(filename):
    """open the file, choose a line"""
    with open(f'data/{filename}', encoding="UTF-8") as text_file:
        return random.choice(text_file.readlines()).strip()

def adjective():
    """give me a random adjective"""
    return get_word('adjectives.txt').capitalize()

def noun():
    """give me a random noun"""
    return get_word('nouns.txt').capitalize()


def verb():
    """give me a random verb"""
    return get_word('verbs.txt').capitalize()

def place():
    """give me a random British place"""
    return get_word('places.txt')

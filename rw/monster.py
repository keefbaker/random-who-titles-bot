import random

monsters = [
    {"s": "dalek", "p": "daleks"},
    {"s": "cybernam", "p": "cybermen"},
    {"s": "sea devil", "p": "sea devils"},
    {"s": "angel", "p": "angels"},
    {"s": "silurian", "p": "silurians"},
    {"s": "master", "p": "master"},
    {"s": "sontaran", "p": "sontarans"},
    {"s": "rutan", "p": "rutans"},
    {"s": "bandrill", "p": "bandrills"},
    {"s": "vashta nerada", "p": "vashta nerada"},
    {"s": "dinosaur", "p": "dinosaurs"},
    {"s": "planet", "p": "planets"},
    {"s": "doctor", "p": "doctors"},
    {"s": "chumbly", "p": "chumblies"},
    {"s": "terileptil", "p": "terileptils"},
    {"s": "judoon", "p": "judoon"},
    {"s": "zygon", "p": "zygons"},
]

monsters += [{"s": "dalek", "p": "daleks"}] * 5
monsters += [{"s": "cybernam", "p": "cybermen"}] * 4
monsters += [{"s": "master", "p": "master"}] * 3
monsters += [{"s": "sontaran", "p": "sontarans"}] * 2


class Monster:
    def __init__(self):
        self.singular = ""
        self.plural = ""
        self.populate()

    def populate(self):
        monster = random.choice(monsters)
        self.singular = monster["s"]
        self.plural = monster["p"]

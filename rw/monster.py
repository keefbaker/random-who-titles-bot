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
    def __init__(self):
        self.singular = ""
        self.plural = ""
        self.populate()

    def populate(self):
        monster = random.choice(monsters)
        self.singular = monster["s"]
        self.plural = monster["p"]

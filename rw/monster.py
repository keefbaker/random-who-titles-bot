import random

monsters = [
    {
        "s" : "dalek",
        "p" : "daleks"
    },
    {
        "s": "cybernam",
        "p": "cybermen"
    },
    {
        "s": "sea devil",
        "p": "sea devils"
    },
    {
        "s": "angel",
        "p": "angels"
    },
    {
        "s": "silurian",
        "p": "silurians"
    },
    {
        "s": "master",
        "p": "master"
    },
    {
        "s": "sontaran",
        "p": "sontarans"
    },
    {
        "s": "rutan",
        "p": "rutans"
    },
    {
        "s": "bandrill",
        "p": "bandrills"
    },
    {
        "s": "vashta nerada",
        "p": "vashta nerada"
    },
    {
        "s": "tory",
        "p": "tories"
    },
    {
        "s": "chumbly",
        "p": "chumblies"
    },
    {
        "s": "terileptil",
        "p": "terileptils"
    },
    {
        "s": "judoon",
        "p": "judoon"
    },
    {
        "s": "zygon",
        "p": "zygons"
    }
]

class Monster:

    def __init__(self):
        self.singular = ""
        self.plural = ""
        self.populate()

    def populate(self):
        monster = random.choice(monsters)
        self.singular = monster["s"]
        self.plural = monster["p"]

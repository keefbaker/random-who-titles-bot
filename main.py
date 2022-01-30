import sys
import random
from rw.nouns import noun
from rw.verbs import verb
from rw.monster import Monster
from rw.places import place
from rw.config import get_config
from rw.tweet import tweet_it

doctors = [
    "Willam Hartnell",
    "Peter Cushing",
    "Patrick Troughton",
    "Jon Pertwee",
    "Tom Baker",
    "Peter Davison",
    "Colin Baker",
    "Sylvester McCoy",
    "Paul McGann",
    "Christopher Eccleston",
    "David Tennant",
    "Matt Smith",
    "Peter Capaldi",
    "Jodie Whittaker",
    "Jo Martin",
]


def get_episode_title():
    monster = Monster()
    sentences = [
        f"{noun().capitalize()} of the {monster.plural.capitalize()}.",
        f"{noun().capitalize()} for the {monster.plural.capitalize()}.",
        f"{noun().capitalize()} of the {monster.plural.capitalize()}.",
        f"The {monster.plural.capitalize()} {verb().capitalize()}.",
        f"The {monster.singular.capitalize()} {noun().capitalize()}.",
        f"{monster.plural.capitalize()} in {place()}!",
        f"{monster.plural.capitalize()} {verb().capitalize()} {place()}",
        f"{verb().capitalize()} the {monster.singular.capitalize()}.",
        f"{noun().capitalize()} of the {monster.plural.capitalize()}!",
    ]

    return random.choice(sentences)


def get_hashtag():
    hashtags = ["", "#DoctorWho", "#DrWho", "#DoctorWhoFlux", "#TARDIS"]
    return random.choice(hashtags)


episode = get_episode_title()
hashtag = get_hashtag()

if len(sys.argv) > 1 and sys.argv[1] == "test":
    print(episode)
    sys.exit(0)

message = f"{episode} starring {random.choice(doctors)} {hashtag}"
config = get_config("./config.yaml")
tweet_it(message, config)

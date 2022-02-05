"""
This will choose random Doctor Who episodes for you
"""
import sys
import random
from rw.words import noun, verb, adjective, Monster, place
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
    "John Hurt",
    "Christopher Eccleston",
    "David Tennant",
    "Matt Smith",
    "Peter Capaldi",
    "Jodie Whittaker",
    "Jo Martin",
]


def get_episode_title(randomize=True):
    """
    get monsters and if randomize is set then send back
    one random sentence, otherwise populate them all
    (used for testing)
    """
    monster = Monster()
    monster_two = Monster()
    while monster.singular == monster_two.singular:
        monster_two.replace()
    sentences = [
        f"{noun()} of the {monster.plural}",
        f"{noun()} for the {monster.plural}",
        f"{noun()} of the {monster.plural}",
        f"The {monster.plural} {verb()}",
        f"The {monster.singular} {noun()}",
        f"{monster.plural} in {place()}",
        f"{monster.plural} {verb()} {place()}",
        f"{verb()} the {monster.singular}",
        f"{noun()} of the {monster.plural}",
        f"{monster.plural} vs {monster_two.plural}",
        f"The {adjective()} {noun()}",
        f"The {adjective()} {monster.singular}",
        f"{adjective()} {monster.plural}, {adjective()} {monster.plural}",
    ]
    if randomize:
        return random.choice(sentences)
    return sentences


def get_hashtag():
    """give me a hashtag"""
    hashtags = ["", "#DoctorWho", "#DrWho", "#DoctorWhoFlux", "#TARDIS"]
    return random.choice(hashtags)


episode = get_episode_title()
hashtag = get_hashtag()

if len(sys.argv) > 1 and sys.argv[1] == "test":
    episodes = get_episode_title(False)
    for episode in episodes:
        print(episode)
    sys.exit(0)

message = f"{episode}, starring {random.choice(doctors)}. {hashtag}"
config = get_config("./config.yaml")
tweet_it(message, config)

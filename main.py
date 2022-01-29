import random
from rw.nouns import noun
from rw.verbs import verb
from rw.monster import Monster
from rw.places import place
from rw.config import get_config
from rw.tweet import tweet_it

monster = Monster()
sentences = [
f'{noun().capitalize()} of the {monster.plural.capitalize()}.',
f'{noun().capitalize()} of the {monster.plural.capitalize()}',
f'{verb().capitalize()} the {monster.plural.capitalize()}',
f'The {monster.plural.capitalize()} {verb()}',
f'{monster.plural.capitalize()} {verb()}',
f'{monster.plural.capitalize()} in {place()}',
f'{monster.plural.capitalize()} {verb()} {place()}',
f'{noun().capitalize()} the {monster.singular}',
f'{noun().capitalize()} of the {monster.plural.capitalize()}!',
f'The Doctor will {verb()} the {noun()}'
]

episode = random.choice(sentences)
config = get_config("./config.yaml")


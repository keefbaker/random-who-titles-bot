import random
from rw.nouns import noun
from rw.verbs import verb
from rw.monster import Monster
from rw.places import place

monster = Monster()
sentences = [
f'{noun().capitalize()} of the {monster.plural.capitalize()}',
f'{noun().capitalize()} of the {monster.plural.capitalize()}',
f'{noun().capitalize()} of the {monster.plural.capitalize()}',
f'The {monster.plural.capitalize()} {verb()}',
f'A {monster.singular} {verb()}s',
f'The {monster.plural} {noun()}',
f'{monster.plural.caplitalize()} in {place()}'
f''
]

print(random.choice(sentences))

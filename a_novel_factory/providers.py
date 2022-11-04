import random
from faker import Faker
from faker.providers import BaseProvider
from a_novel_factory.corpora import Corpora

fake = Faker()
corpora = Corpora()


class CustomSentenceProvider(BaseProvider):
    def custom_sentence(self, characters) -> str:
        # base text
        text = fake.sentence()

        random_value = random.random()

        if random_value < 0.5:
            return f'{text}'
        elif random_value < 0.8:
            # one-character sentences
            c = random.choice(characters)
            a = random.choice(corpora.activities)
            return random.choice([
                f'{c.name} said "{text}"',
                f'{c.first} thought "{text}"',
                f'Look at {c.first} go!',
                f'{c.name} wept.',
                f'{c.name} took a cab.',
                f"{c.prefix} {c.last}'s shoes were too tight.",
                f'{c.name} sang, "{text}"',
                f'{c.first} was {a}.'
            ])
        else:
            # two-character sentences
            c1, c2 = random.sample(characters, k=2)
            return random.choice([
                f'{c1.first} greeted {c2.first}.',
                f'{c1.name} fell in love with {c2.name}.',
                f'{c1.name} eyed {c2.name}.',
                f'{c1.first} asked {c2.first} for the time.',
                f'"{c1.prefix} {c1.last}, I presume," said {c2.name}.'
            ])

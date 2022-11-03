import factory
from a_novel_factory import objects, providers
from random import randint, sample
from faker import Faker

fake = Faker()
fake.add_provider(providers.CustomSentenceProvider)


class TitleFactory(factory.Factory):
    class Meta:
        model = objects.Title

    title = factory.Faker('sentence', nb_words=3, variable_nb_words=True)


class SentenceFactory(factory.Factory):
    class Meta:
        model = objects.Sentence

    text = factory.LazyAttribute(
        lambda o: fake.custom_sentence(o.characters)
    )


class CharacterFactory(factory.Factory):
    class Meta:
        model = objects.Character

    first = factory.Faker('first_name')
    last = factory.Faker('last_name')
    prefix = factory.Faker('prefix')


class ParagraphFactory(factory.Factory):
    class Meta:
        model = objects.Paragraph

    sentences = factory.LazyAttribute(
        lambda o: SentenceFactory.create_batch(randint(2, 24),
                                               characters=o.characters)
    )


class ChapterFactory(factory.Factory):
    class Meta:
        model = objects.Chapter

    number = factory.Sequence(lambda n: n + 1)
    title = factory.LazyAttribute(lambda _: TitleFactory.create())
    characters = factory.LazyAttribute(
        lambda o: sample(o.novel_characters, k=randint(2, 4))
    )

    paragraphs = factory.LazyAttribute(
        lambda o: ParagraphFactory.create_batch(randint(10, 30),
                                                characters=o.characters)
    )


class NovelFactory(factory.Factory):
    class Meta:
        model = objects.Novel

    title = factory.SubFactory(TitleFactory)
    characters = CharacterFactory.create_batch(randint(4, 18))
    chapters = ChapterFactory.create_batch(randint(40, 50),
                                           novel_characters=characters)

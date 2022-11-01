import factory
from a_novel_factory import objects
from random import randint


class TitleFactory(factory.Factory):
    class Meta:
        model = objects.Title

    title = factory.Faker('sentence', nb_words=3, variable_nb_words=True)


class SentenceFactory(factory.Factory):
    class Meta:
        model = objects.Sentence

    text = factory.Faker('sentence')


class ParagraphFactory(factory.Factory):
    class Meta:
        model = objects.Paragraph

    sentences = factory.LazyAttribute(
        lambda _: SentenceFactory.create_batch(randint(2, 24))
    )


class ChapterFactory(factory.Factory):
    class Meta:
        model = objects.Chapter

    number = factory.Sequence(lambda n: n + 1)
    title = factory.LazyAttribute(lambda _: TitleFactory.create())
    paragraphs = factory.LazyAttribute(
        lambda _: ParagraphFactory.create_batch(randint(10, 30))
    )


class NovelFactory(factory.Factory):
    class Meta:
        model = objects.Novel

    title = factory.SubFactory(TitleFactory)
    chapters = ChapterFactory.create_batch(randint(40, 50))

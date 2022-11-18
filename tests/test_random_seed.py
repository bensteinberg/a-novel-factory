import pytest
from a_novel_factory import factories
from a_novel_factory.util import set_seed


def test_set_seed():
    """
    Confirm that setting the random seed results in generating the same
    novel twice -- this is flawed, since resetting seeds in a single session
    doesn't work
    """
    set_seed('hello')
    novel1 = factories.NovelFactory()
    set_seed('hello')
    novel2 = factories.NovelFactory()

    # these are in fact different objects
    assert novel1 != novel2

    # different title generators should produce the same output
    assert novel1.title != novel2.title
    assert str(novel1.title) == str(novel2.title)

    assert len(novel1.chapters) == len(novel2.chapters)
    for i in range(len(novel1.chapters)):
        assert len(
            novel1.chapters[i].paragraphs
        ) == len(
            novel2.chapters[i].paragraphs
        )
        # why are these objects the same when the novel title objects
        # are not? is one lazy and the other not? checking....
        # yes: the Novel uses factory.SubFactory(TitleFactory) while the
        # Chapter uses factory.LazyAttribute(lambda _: TitleFactory.create()),
        # so the objects as well as the outputs are equal
        assert novel1.chapters[i].title == novel2.chapters[i].title
        assert str(novel1.chapters[i].title) == str(novel2.chapters[i].title)
        for j in range(len(novel1.chapters[i].paragraphs)):
            assert (
                novel1.chapters[i].paragraphs[j]
            ) == (
                novel2.chapters[i].paragraphs[j]
            )
            assert str(
                novel1.chapters[i].paragraphs[j]
            ) == str(
                novel2.chapters[i].paragraphs[j]
            )


@pytest.mark.xfail(reason="setting seeds twice in one session doesn't work")
def test_different_seeds():
    """
    Confirm that setting different random seeds results in different novels...
    """
    set_seed('hello')
    novel1 = factories.NovelFactory()
    set_seed('goodbye')
    novel2 = factories.NovelFactory()

    # these are in fact different objects
    assert novel1 != novel2

    # different title generators should produce different output
    assert novel1.title != novel2.title
    assert str(novel1.title) != str(novel2.title)

    assert len(novel1.chapters) != len(novel2.chapters)

    for i in range(len(novel1.chapters)):
        assert len(
            novel1.chapters[i].paragraphs
        ) != len(
            novel2.chapters[i].paragraphs
        )
        for j in range(len(novel1.chapters[i].paragraphs)):
            assert str(
                novel1.chapters[i].paragraphs[j]
            ) != str(
                novel2.chapters[i].paragraphs[j]
            )

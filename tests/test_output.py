from a_novel_factory import factories


def test_output_length():
    """
    Confirm output is large enough -- run repeatedly, for example:
    $ for n in `seq 1 100` ; do poetry run pytest ; done
    (we can't do the repetition here, because the outputs will be
    the same -- but why are the outputs slightly different?)
    I have seen one test failure like this, in hundreds of runs...
    """
    novel = factories.NovelFactory()
    assert len(f'{novel}'.split()) > 50000

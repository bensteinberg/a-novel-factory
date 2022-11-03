from a_novel_factory import factories


def test_character_lists():
    """
    Confirm that each chapter, paragraph, and sentence have the appropriate
    sublists of characters, and that all are subsets of the novel's characters.
    """
    novel = factories.NovelFactory()

    for chapter in novel.chapters:
        assert all([c in novel.characters for c in chapter.characters])
        assert len(chapter.characters) <= len(novel.characters)
        for paragraph in chapter.paragraphs:
            assert paragraph.characters == chapter.characters
            for sentence in paragraph.sentences:
                assert sentence.characters == paragraph.characters

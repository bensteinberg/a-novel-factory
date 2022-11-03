from importlib import metadata

__version__ = metadata.version(__package__)


class Novel:
    def __init__(self, title, chapters, characters):
        self.title = title
        self.chapters = chapters
        self.characters = characters

    def __str__(self):
        title = f'{self.title}'
        frontmatter = (
            '---\n'
            f'title: "{title}"\n'
            f'creator: {__package__} {__version__}\n'
            '---\n'
        )
        body = f'# {title.upper()} #\n\n' + '\n\n\n'.join(
            [str(c) for c in self.chapters]
        )
        return frontmatter + body


class Chapter:
    def __init__(self, number, title, novel_characters, characters,
                 paragraphs):
        self.number = number
        self.title = title
        self.novel_characters = novel_characters
        self.characters = characters
        self.paragraphs = paragraphs

    def __str__(self):
        return f'## Chapter {self.number}: {self.title} ##\n\n' + '\n\n'.join(
            [str(p) for p in self.paragraphs]
        )


class Paragraph:
    def __init__(self, sentences, characters):
        self.sentences = sentences
        self.characters = characters

    def __str__(self):
        return ' '.join([str(s) for s in self.sentences])


class Sentence:
    def __init__(self, text, characters):
        self.text = text
        self.characters = characters

    def __str__(self):
        return f'{self.text}'


class Title:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        # remove period at the end of the "sentence"
        return f'{self.title}'[0:-1]


class Character:
    def __init__(self, first, last, prefix):
        self.first = first
        self.last = last
        self.name = f'{first} {last}'
        self.prefix = prefix

    def __str__(self):
        return f'{self.prefix} {self.name}'

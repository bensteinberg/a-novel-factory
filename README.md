a-novel-factory
===============

This is an entry for [NaNoGenMo
2022](https://github.com/NaNoGenMo/2022). It is an experiment in the
(mis)use of
[factory_boy](https://factoryboy.readthedocs.io/en/stable/) and
[Faker](https://faker.readthedocs.io/en/master/), Python packages used
to create test fixtures.

For those not already familiar with software testing, the basic idea
is that by writing (and automating) tests of program components and
the overall function of a program, you can be (more) confident that a
given change to your program does not add (as many) new bugs. You
frequently want to test the operation of the program or its components
with particular inputs, and although you might hand-code these inputs,
known as fixtures, it is easier to use a system like `factory_boy` to
generate them for you. `Faker` is used by `factory_boy` to produce
fake data, like names or addresses, to populate these fixtures.

The misuse of `factory_boy` and `Faker` is to create a "factory" not
for producing test fixtures, but for producing a "novel"---a text of
at least 50,000 words. This code creates
[factories](a_novel_factory/factories.py) for Novel, Chapters,
Paragraphs, Sentences, and Titles, from bare specifications called
[objects](a_novel_factory/objects.py). (In other contexts, the objects
would be the actual data models used by the application under test.)
In the initial version of this code, the factories at the bottom
level---Sentences and Titles---use `Faker`'s [lorem
Provider](https://faker.readthedocs.io/en/master/providers/faker.providers.lorem.html)
to generate random text. With any luck, future versions will enhance
the output with a [Dynamic
Provider](https://faker.readthedocs.io/en/master/#how-to-create-a-dynamic-provider),
possibly using [corpora](https://github.com/dariusk/corpora) as raw
material.

At the moment, the output is entirely random. Another possible
enhancement is to set the random seed, so that particular outputs are
repeatable.

A [sample output](output/0.1.0-place_improve.md) in Markdown format is
in this repo, as well as [PDF](output/0.1.0-place_improve.pdf) and
[epub](output/0.1.0-place_improve.epub) versions.

Usage
-----

Clone this repo, [install
Poetry](https://python-poetry.org/docs/#installation), optionally
[install Pandoc](https://pandoc.org/installing.html), then run

```
cd a-novel-factory
poetry install
poetry run new_novel
```

This will generate Markdown, PDF, and epub files, using the novel's
title as filename. `poetry run new_novel --no-title-from-text` will
generate `a_novel.[md|pdf|epub]`. In the absence of Pandoc, only
Markdown will be produced. (Note that on some Macs, with Pandoc
installed, if you get an error like `pandoc: pdflatex: createProcess:
posix_spawnp: illegal operation (Inappropriate ioctl for device)`, you
may need to install or reinstall `pdflatex`, possibly with `brew
reinstall --cask basictex`.)

Credit
------

Thanks to @lizadaly for telling us about NaNoGenMo!

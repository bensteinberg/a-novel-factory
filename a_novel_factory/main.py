import click
import humanize
import subprocess
from importlib import metadata

__version__ = metadata.version(__package__)


@click.command()
@click.option('--output-dir', '-o', default='./output')
@click.option('--seed', help='Random seed')
def new_novel(output_dir, seed):
    """
    Writes a generated novel to a Markdown file. Outputs PDF and epub files
    if pandoc is installed.
    """
    if seed:
        from a_novel_factory.util import set_seed
        set_seed(seed)

    from a_novel_factory import factories
    novel = factories.NovelFactory(seed=seed)

    title = f'{__version__}-{novel.title}'.replace(' ', '_').lower()

    text = f'{novel}'
    with open(f'{output_dir}/{title}.md', 'w') as md:
        md.write(text)

    length = humanize.intcomma(len(text.split()))
    click.echo(f'Wrote {output_dir}/{title}.md, approximately {length} words')

    try:
        for fmt in ['pdf', 'epub']:
            subprocess.run(f'pandoc {output_dir}/{title}.md '
                           f'-o {output_dir}/{title}.{fmt}',
                           shell=True)
            click.echo(f'Wrote {output_dir}/{title}.{fmt}')
    except FileNotFoundError:
        click.echo('You must have pandoc installed to produce PDF and epub')

import click
import humanize
import subprocess
from importlib import metadata
from a_novel_factory import factories

__version__ = metadata.version(__package__)


@click.command()
@click.option('--output-dir', '-o', default='./output')
def new_novel(output_dir):
    """
    Writes a generated novel to a Markdown file. Outputs PDF and epub files
    if pandoc is installed.
    """
    novel = factories.NovelFactory()

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

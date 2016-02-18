"""CLI for finding and grouping
all files in a directory, and then
moving each group of files into their own
file in a different directory"""
import sys
import os
import re
import shutil
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def get_groups(pat, inputs):
    """
    Get all the groups we have.
    """
    p = re.compile(pat)
    groups = set(m.group() for m in
                 [p.search(i) for i in inputs]
                 if m)
    return groups


def get_files(path='.'):
    """Get all file names from a given path"""
    return [x.name for x in os.scandir(path) if x.is_file()]


def move_files(groups, files, filedir='.', head_dir='.', copy=False, verbosity=1):
    """
    Move files to new directory.
    Create directory if does not exist.
    """
    for group in groups:
        if verbosity:
            click.echo('\nGroup {} \n{}\n'.format(group, '-'*9))
        p = re.compile(group)
        target_dir = os.path.join(head_dir, group)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
        targets = [(os.path.join(filedir, x), os.path.join(target_dir, x))
                   for x in files if p.search(x)]

        for target in targets:
            if verbosity:
                click.echo('{} -> {}'.format(click.format_filename(target[0]),
                                             click.format_filename(target[1]))
                )

            if copy:
                shutil.copy2(target[0], target[1])
            elif not copy:
                shutil.move(target[0], target[1])

    return


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-c', '--copy', is_flag=True,
              help='Copy files to new folder instead of moving.')
@click.option('-v/-q', '--verbosity/--quiet', default=True,
              help='Toggle verbose/quiet.')
@click.argument('source', type=click.Path(exists=True))
@click.argument('target', type=click.Path(exists=True))
@click.argument('pattern', type=str)
def cli(source, target, pattern, copy, verbosity):
    """CLI for sorting files from one folder into individual 
    folders for files with similar names.

    Parameters\n
    ----------

    SOURCE : source directory with files needing to be grouped\n
        (must exist)

    TARGET : target directory where new folders will be place\n
        (must exist)

    PATTERN : regular expression pattern for grouping files\n
        (enclose this in quotation marks)


    ---------

    Example to group all files based on first 5 letters:\n

    $groupfiles ./junk_folder ./sorted_stuff '^[a-zA-Z]{5}'

    ---------

    Other examples of regular expression patterns that may be useful:

    '^' : (Caret) start your regular expression with this to match\n
        at start of string

    '.' : (Dot) any character

    '+' : (Plus) one or more repetitions of the preceeding expression

    '*' : (Star) 0 or more repetitions of the preceeding expression

    '?' : 0 or 1 repetitions of the preceeding expression

    {m} : Exactly m copies of the preceeding expression

    {m,n} : From m to n copies of the preceeding expression

    \d : digit
    
    Put together :

    ^/d{5}.+/d{5} : 5 digits, then 1 or more of any character,\n
        then 5 more digits.

    """
    if copy and verbosity:
        click.echo('Copying files instead of moving.')

    files = get_files(source)
    groups = get_groups(pattern, files)
    if len(groups) == 0:
        click.echo('No file groups found!')
        sys.exit(0)
    if verbosity:
        click.echo('\nHere are all of the found groups:')
        [click.echo(group) for group in groups]
    move_files(groups, files, source, target, copy=copy, verbosity=verbosity)

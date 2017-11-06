"""
Mario CLI scripts
"""
import os
import click

class Config(object): #pylint: disable=too-few-public-methods
    """
    Helper class to pass config through the click app.
    """

    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug

@click.group()
@click.option('--debug', is_flag=True)
@click.pass_context
def cli(ctx, debug=False):
    """
    Base application/group. Subcommands 'extend' the options/args.
    """
    ctx.obj = Config(debug=debug)

@cli.command(name="about")
def about():
    """
    Learn more about mario
    """
    click.echo(
        """
        Hello! Welcome to mario.

        mario is a tool for working with remote content.
        It works well with endpointer and static site generators.

        mario currently works well with content formatted for
        Hugo (gohugo.io) but support for other content is welcomed!
        """
    )


if __name__ == '__main__':
    about()

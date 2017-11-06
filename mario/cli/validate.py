"""
Mario CLI 'validate' subcommand

Usage: mario validate [OPTIONS]

Options:
  --help           Show this message and exit.
  --verbose        Verbose output

Proposed options:
  -f the file to validate (e.g. if not in an active content package)
"""
import os

import click
import pkg_resources
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import yaml, json
from .cli import cli


@cli.command(name="validate")
@click.pass_context
def endpoints_command(ctx):
    """
    Validates .platform.yml in $PWD
    """

    # TODO: Wrap this in a try and have excellent exception handling.
    schema_string = pkg_resources.resource_stream(
        __name__,
        'schema/mariov1.json'
    ).read().decode()
    schema = json.loads(schema_string)

    # TODO: This should be an input param and not hard coded.
    if not os.path.isfile('.platform.yml'):
        raise Exception("Expected .platform.yml in current directory.")


    with open('.platform.yml') as platform_spec_file:
        platform_spec = yaml.load(platform_spec_file.read())

    # TODO: This could do with a --verbose flag for more useful output
    try:
        validate(platform_spec, schema)
        click.secho('Success! Your .platform.yml is valid!', fg='green')
    except Exception as e:
        click.secho('Failure! Your .platform.yml is NOT valid!', fg='red')
        click.echo(e.message)

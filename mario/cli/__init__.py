"""
Mario CLI

Usage: mario [subcommand] [OPTIONS]

Subcommands:
  validate         Validates your .platform.yml file (TODO)
  update           Compares pinned versions to see if there are new versions (TODO)
  install          Retrieves packaged content and installs it locally (TODO)

Options:
  --help           Show this message and exit.
  --verbose        Verbose output
"""
from .cli import cli
from .validate import validate

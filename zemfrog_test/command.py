import click
import os
from flask.globals import current_app
import pytest

from flask.cli import with_appcontext
from .generator import g_init_test, g_unit_test


@click.group("test")
def group():
    """
    Unit testing tools.
    """


@group.command()
@with_appcontext
def init():
    """
    Initialization projects with unit testing.
    """

    g_init_test()


@group.command()
@click.argument("name")
@with_appcontext
def new(name):
    """
    Create a new unit test.
    """

    g_unit_test(name)


@group.command()
@with_appcontext
def run():
    """
    Run unit tests.
    """

    os.chdir(current_app.root_path)
    pytest.main(["tests"])

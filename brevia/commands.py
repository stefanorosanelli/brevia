"""Utility commands for applications"""
import click
from brevia import alembic


@click.command()
@click.option("-v", "--verbose", is_flag=True, default=False, help="Verbose mode")
def db_current_cmd(verbose):
    """Display current database revision"""
    alembic.current(verbose)


@click.command()
@click.option("-r", "--revision", default="head", help="Revision target")
def db_upgrade_cmd(revision):
    """Upgrade to a later database revision"""
    alembic.upgrade(revision)


@click.command()
@click.option("-r", "--revision", required=True, help="Revision target")
def db_downgrade_cmd(revision):
    """Revert to a previous database revision"""
    alembic.downgrade(revision)
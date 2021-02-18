import click
from backup.component.behaviour.BackupService import BackupService
from getpass import getpass

backupService = BackupService.getInstance()


@click.group()
def main():
    pass


@click.command()
@click.option("--repository", required=True, type=str)
@click.option("--location", required=True, type=str)
@click.option("--password", default=None)
def setup(repository, location, password):
    if password == None:
        password = getpass()
    backupService.setup(repository, location, password)


main.add_command(setup)

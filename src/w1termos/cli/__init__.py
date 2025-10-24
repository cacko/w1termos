
from typing_extensions import Annotated
import rich
import typer
from w1termos.sensor import get_sensors

cli = typer.Typer()


@cli.command()
def ls():
    for sensor in get_sensors():
        rich.print(sensor)

@cli.command()
def get():
    pass
    

@cli.callback()
def main(ctx: typer.Context):
    pass

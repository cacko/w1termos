from typing_extensions import Annotated
import rich
import typer
from w1termos.sensor import get_sensors, get_celcius, get_sensor
import logging

cli = typer.Typer()


@cli.command()
def ls():
    for sensor in get_sensors():
        rich.print(sensor)


@cli.command()
def temp(id: Annotated[str, typer.Argument()] = None):
    try:
        if not id:
            sensor = [sensor for sensor in get_sensors()][0]
        else:
            sensor = get_sensor(id)
        assert sensor
        rich.print(get_celcius(sensor=sensor))
    except Exception as e:
        logging.error(e)


@cli.callback()
def main(ctx: typer.Context):
    pass

import click
from services.owner_service import *
from services.car_service import *
from services.garage_service import *

@click.group()
def cli():
    """Car Owners and Garage Management CLI"""
    pass

# Owner Commands
@cli.group()
def owner():
    """Manage car owners"""
    pass

@owner.command()
def register():
    """Register a new car owner manually via prompts."""
    name = click.prompt("Enter owner's name")
    email = click.prompt("Enter owner's email")
    phone = click.prompt("Enter owner's phone number")
    register_owner(name, email, phone)

# Car Commands
@cli.group()
def car():
    """Manage cars"""
    pass

@car.command()
def add():
    """Add a new car manually via prompts."""
    owner_id = click.prompt("Enter owner ID", type=int)
    make = click.prompt("Enter car make")
    model = click.prompt("Enter car model")
    year = click.prompt("Enter year", type=int)
    vin = click.prompt("Enter VIN")
    add_car(owner_id, make, model, year, vin)

# Garage Commands
@cli.group()
def garage():
    """Manage garages"""
    pass

@garage.command()
def add():
    """Add a new garage manually via prompts."""
    name = click.prompt("Enter garage name")
    location = click.prompt("Enter location")
    capacity = click.prompt("Enter capacity", type=int)
    add_garage(name, location, capacity)

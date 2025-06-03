import click

from services.owner_service import create_owner, get_all_owners
from services.car_service import create_car, get_all_cars, link_car_to_garage
from services.garage_service import create_garage, get_all_garages

@click.group()
def cli():
    """Car Garage Management CLI"""
    pass

# ----- OWNER COMMANDS -----

@cli.command()
@click.option('--name', prompt='Owner name')
@click.option('--phone', prompt='Phone number')
@click.option('--email', prompt='Email', default='', required=False)
def add_owner(name, phone, email):
    owner = create_owner(name, phone, email if email else None)
    click.echo(f"✅ Owner created: {owner}")

@cli.command()
def list_owners():
    owners = get_all_owners()
    for owner in owners:
        click.echo(owner)

# ----- CAR COMMANDS -----

@cli.command()
@click.option('--make', prompt='Car make')
@click.option('--model', prompt='Car model')
@click.option('--year', prompt='Year', type=int)
@click.option('--license', prompt='License plate')
@click.option('--owner_id', prompt='Owner ID', type=int)
def add_car(make, model, year, license, owner_id):
    car = create_car(make, model, year, license, owner_id)
    if car:
        click.echo(f"🚗 Car created: {car}")
    else:
        click.echo("❌ Owner ID not found.")

@cli.command()
def list_cars():
    cars = get_all_cars()
    for car in cars:
        click.echo(car)

@cli.command()
@click.option('--car_id', prompt='Car ID', type=int)
@click.option('--garage_id', prompt='Garage ID', type=int)
def link_car(car_id, garage_id):
    car = link_car_to_garage(car_id, garage_id)
    if car:
        click.echo(f"🔗 Car linked to garage: {car}")
    else:
        click.echo("❌ Invalid car or garage ID.")

# ----- GARAGE COMMANDS -----

@cli.command()
@click.option('--name', prompt='Garage name')
@click.option('--location', prompt='Location')
@click.option('--contact', prompt='Contact number', default='', required=False)
def add_garage(name, location, contact):
    garage = create_garage(name, location, contact if contact else None)
    click.echo(f"🏠 Garage created: {garage}")

@cli.command()
def list_garages():
    garages = get_all_garages()
    for garage in garages:
        click.echo(garage)

if __name__ == "__main__":
    cli()

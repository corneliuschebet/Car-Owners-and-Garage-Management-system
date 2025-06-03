from setuptools import setup, find_packages

setup(
    name="car-garage-mgmt",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "sqlalchemy",
    ],
    entry_points={
        "console_scripts": [
            "add-car=cli.main:add_car",
            "add-owner=cli.main:add_owner",
            "add-garage=cli.main:add_garage",
            "list-cars=cli.main:list_cars",
            "list-owners=cli.main:list_owners",
            "list-garages=cli.main:list_garages",
            "link-car=cli.main:link_car",
        ],
    },
)

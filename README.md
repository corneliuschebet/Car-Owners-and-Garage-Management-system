# Car-Owners-and-Garage-Management-system
## Project Overview

A Python-based CLI application designed to streamline relationships between car owners, their vehicles, and service garages through a robust database system built with SQLAlchemy ORM.

##  The Problem We Solve

Small garages and car owners struggle with fragmented record-keeping systems. Our solution addresses:

### Data Management Challenges
- Scattered service records
- Difficulty tracking vehicle-owner relationships
- Lost maintenance histories

### Operational Inefficiencies
- Time wasted searching customer information
- Manual processes slowing operations

### Customer Experience Issues
- Poor service continuity
- Difficulty accessing service history

## Solution

A centralized CLI management system that creates a hub for all car-garage-owner relationships, enabling efficient data management and streamlined operations.

## Key Features

### For Car Owners
- Vehicle registration with detailed specs
- Garage preference management
- Complete service history tracking

### For Garage Managers
- Comprehensive customer/vehicle records
- Service scheduling
- Business analytics reporting

### For System Administrators
- Full CRUD operations
- Data integrity enforcement
- User access control

## 🛠️ Technical Architecture

    A[CLI Interface] --> B[Business Logic]
    B --> C[SQLAlchemy ORM]
    C --> D[(SQLite Database)]

# Installation    
git clone 
cd Car-Owners-and-Garage-Management-systems
pipenv install
pipenv install sqlalcemy
pipenv shell

# Usage 
pipenv run python -m cli.main [COMMAND]

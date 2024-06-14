# Phase 3 CLI+ORM Project(Hotel Reservation)

## Introduction

The Hotel Reservation System is a command-line interface (CLI) application built with Python. It allows different types of users to perform various operations related to hotel reservations. The system supports CRUD (Create, Read, Update, Delete) functionality and uses an Object-Relational Mapping (ORM) for database interactions.


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/KiokoB/my_project_hotel
    cd my_project_hotel
    ```
2. **Getting a virtual environment:**
    ```bash
    pipenv install
    pipenv shell  
    ```
3. **Install dependencies:**
    ```bash
    pip install <dependencies>
    ```
4. **Accessing the database:**
    You can install SQLite Viewer as an extension in VSCode using the link provided below:
    https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer
    You can also "DB Browser for SQLite" 


## Features

- **Client:** 
  - See a list of available hotels
  - View employees available

- **Employee:**
  - View all clients
  - Be assigned duties

- **Hotel Administration:**
  - Manage employees
  - View all clients 

- **General:**
  - CRUD operations for hotels, clients, and employees
  - ORM integration for seamless database management

## Usage
- To start the apllication, run:
    ```bash
    ./lib/cli.py


## Resources

- [https://moringa.instructure.com/courses/703/pages/phase-3-cli+orm-project-template]
- [https://docs.python.org/3/]

#lib/seed.py
from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.client import Client
from models.hotel import Hotel


def hotel_database():
    Hotel.drop_table
    Client.drop_table()
    Employee.drop_table()
    Employee.create_table()
    Client.create_table()
    Hotel.create_table()
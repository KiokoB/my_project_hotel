#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.employee import Employee
from models.client import Client
from models.hotel import Hotel

import ipdb

def reset_database():
    Hotel.drop_table()
    Employee.drop_table()
    Client.drop_table()
    Client.create_table()
    Employee.create_table()
    Hotel.create_table()

    employee1 = Employee.create("Ken", "Manager")
    # employee1.name = 'Jaime'
    # employee1.duty_assigned = 'Receptionist'
    #employee1.update()
    #employee1.delete()

    client1 = Client.create("Linde", "4th Street", "Board Meeting")
    print(client1)

reset_database()
ipdb.set_trace()

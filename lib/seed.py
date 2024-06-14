#!/usr/bin/env python3

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

    #Hotels data
    Hotel.create("Sarova Panafric Hotel", "Kenyatta Avenue", "0709 111000")
    Hotel.create("Ole Sereni Hotel", "Opposite Nairobi National Park","0732 191000")
    Hotel.create("Laico Regency Hotel", "Nairobi Central Loita St", "020 2211199")
    Hotel.create("Enashipai Resort & Spa", "Moi S Lake Rd,Naivasha", "0719 051000")


    #Employees data
    Employee.create("Ken", "Manager", 1)
    Employee.create("James", "Housekeeping staff", 2)
    Employee.create("Jane", "Receptionist", 1)
    Employee.create("Kyla", "Main Chef", 3)

    #Clients data
    Client.create("Fatima", "Mombasa","Accomodation", 4)
    Client.create("Doe", "Nairobi CBD", "Fine Dining", 4)
    Client.create("Elanor", "Tanzania", "Accomodation", 2)
    Client.create("Barak", "Karen", "Meeting space", 3)


hotel_database()
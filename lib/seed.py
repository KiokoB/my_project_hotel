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
    ht1 = Hotel.create("Sarova Panafric Hotel", "Kenyatta Avenue", "0709 111000")
    ht2 = Hotel.create("Ole Sereni Hotel", "Opposite Nairobi National Park","0732 191000")
    ht3 = Hotel.create("Laico Regency Hotel", "Nairobi Central Loita St", "020 2211199")
    ht4 = Hotel.create("Enashipai Resort & Spa", "Moi S Lake Rd,Naivasha", "0719 051000")


    #Employees data
    Employee.create("Ken", "Manager", ht1.id)
    Employee.create("James", "Housekeeping staff", ht2.id)
    Employee.create("Jane", "Receptionist", ht1.id)
    Employee.create("Kyla", "Main Chef", ht3.id)

    #Clients data
    Client.create("Fatima", "Mombasa","Accomodation", ht4.id)
    Client.create("Doe", "Nairobi CBD", "Fine Dining", ht4.id)
    Client.create("Elanor", "Tanzania", "Accomodation", ht2.id)
    Client.create("Barak", "Karen", "Meeting space", ht3.id)


hotel_database()
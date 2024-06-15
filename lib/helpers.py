# lib/helpers.py
from models.hotel import Hotel
from models.client import Client
from models.employee import Employee

import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)


def enter_program():
    print(Back.MAGENTA + Fore.BLACK +"Hello user, please input your name and password.")
    name = input(Fore.BLUE + "Enter your name here: ")
    password = input(Fore.BLUE + "Enter your password: ")
    print(Back.MAGENTA + Fore.BLACK + f"Welcome {name} to our hotel program!")

def exit_program():
    print(Back.MAGENTA + Fore.BLACK + "Thank you for using our system.Goodbye!")
    exit()

#Hotel data
def list_hotels():
    hotels = Hotel.get_all()
    for hotel in hotels:
        print(hotel)

def find_hotel_by_name():
    name = input(Fore.YELLOW + "Enter the hotel's name: ")
    hotel = Hotel.find_by_name(name)
    print(hotel) if hotel else print(
        Fore.RED + f'Hotel {name} not found')
    
def find_hotel_by_id():
    id_ = input(Fore.YELLOW + "Enter the hotel's id: ")
    hotel = Hotel.find_by_id(id_)
    print(hotel) if hotel else print(Fore.RED + f'Hotel {id_} not found')

def create_hotel():
    name = input(Fore.YELLOW + "Enter the hotel's name: ")
    location = input(Fore.YELLOW + "Enter the hotel's address: ")
    contact = input(Fore.YELLOW + "Enter the hotel's contact: ")
    try:
        hotel = Hotel.create(name, location, contact)
        print(f'Successfully added: {hotel}')
    except Exception as exc:
        print(Fore.RED + "Error creating hotel: ", exc)

def update_hotel():
    id_ = input(Fore.YELLOW + "Enter the hotel's id: ")
    if hotel := Hotel.find_by_id(id_):
        try:
            name = input(Fore.YELLOW + "Enter the hotel's new name: ")
            hotel.name = name
            location = input(Fore.YELLOW + "Enter the new hotel's location: ")
            hotel.location = location
            contact = input(Fore.YELLOW + "Enter the hotel's new contact: ")
            hotel.contact = contact

            hotel.update()
            print(f'Successfully updated: {hotel}')
        except Exception as exc:
            print(Fore.RED + "Error updating hotel: ", exc)
    else:
        print(Fore.RED + f'Hotel {id_} not found')

def delete_hotel():
    id_ = input(Fore.YELLOW + "Enter the hotel's id: ")
    if hotel := Hotel.find_by_id(id_):
        hotel.delete()
        print(f'Hotel {id_} deleted')
    else:
        print(Fore.RED + f'Hotel {id_} not found')


#Clients data
def create_client():
    name = input(Fore.YELLOW + "Enter the client's name: ")
    address = input(Fore.YELLOW + "Enter the client's address: ")
    needs = input(Fore.YELLOW + "Enter the client's needs: ")
    hotel_id = input(Fore.YELLOW + "Enter the client's hotel id: ")
    try:
        client = Client.create(name, address, needs, hotel_id)
        print(f'Successfully added: {client}')
    except Exception as exc:
        print(Fore.RED + "Error creating client: ", exc)

def list_clients():
    clients = Client.get_all()
    for client in clients:
        print(client)

def find_client_by_name():
    name = input(Fore.YELLOW + "Enter the client's name: ")
    client = Client.find_by_name(name)
    print(client) if client else print(
        Fore.RED + f'Client {name} not found')
    
def find_client_by_id():
    id_ = input(Fore.YELLOW + "Enter the client's id: ")
    client = Client.find_by_id(id_)
    print(client) if client else print(Fore.RED + f'Client {id_} not found')

def update_client():
    id_ = input(Fore.YELLOW + "Enter the client's id: ")
    if client := Client.find_by_id(id_):
        try:
            name = input(Fore.YELLOW + "Enter the client's new name: ")
            client.name = name
            address = input(Fore.YELLOW + "Enter the client's new address: ")
            client.address = address
            needs = input(Fore.YELLOW + "Enter the client's new needs: ")
            client.needs = needs
            hotel_id = input(Fore.YELLOW + "Enter the client's new hotel id: ")
            client.hotel_id = hotel_id

            client.update()
            print(f'Successfully updated: {client}')
        except Exception as exc:
            print(Fore.RED + "Error updating client: ", exc)
    else:
        print(Fore.RED + f'Client {id_} not found')

def delete_client():
    id_ = input(Fore.YELLOW + "Enter the client's id: ")
    if client := Client.find_by_id(id_):
        client.delete()
        print(f'Client {id_} deleted')
    else:
        print(Fore.RED + f'Client {id_} not found')

def list_hotel_clients():
    id_ = input(Fore.YELLOW + "Enter the hotel's id: ")
    if hotel := Hotel.find_by_id(id_):
        for client in hotel.clients():
            print(client)
    else:
        print(Fore.RED + f'Hotel {id_} not found')

#Employees data
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input(Fore.YELLOW + "Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        Fore.RED + f'Employee {name} not found')

def find_employee_by_id():
    id_ = input(Fore.YELLOW + "Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(Fore.RED + f'Employee {id_} not found')

def create_employee():
    name = input(Fore.YELLOW + "Enter the employee's name: ")
    duty_assigned = input(Fore.YELLOW + "Enter the employee's duty: ")
    hotel_id = input(Fore.YELLOW + "Enter the employee's hotel id: ")
    try:
        employee = Employee.create(name, duty_assigned, hotel_id)
        print(f'Successfully added: {employee}')
    except Exception as exc:
        print(Fore.RED + "Error creating employee: ", exc)

def update_employee():
    id_ = input(Fore.YELLOW + "Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input(Fore.YELLOW + "Enter the employee's new name: ")
            employee.name = name
            duty_assigned = input(Fore.YELLOW + "Enter the employee's new duty assigned: ")
            employee.duty_assigned = duty_assigned
            hotel_id = input(Fore.YELLOW + "Enter the employee's new hotel id: ")
            employee.hotel_id = hotel_id

            employee.update()
            print(f'Successfully updated: {employee}')
        except Exception as exc:
            print(Fore.RED + "Error updating employee: ", exc)
    else:
        print(Fore.RED + f'Employee {id_} not found')

def delete_employee():
    id_ = input(Fore.YELLOW + "Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(Fore.RED + f'Employee {id_} not found')

def list_hotel_employees():
    id_ = input(Fore.YELLOW + "Enter the hotel's id: ")
    if hotel := Hotel.find_by_id(id_):
        for employee in hotel.employees():
            print(employee)
    else:
        print(Fore.RED + f'Hotel {id_} not found')

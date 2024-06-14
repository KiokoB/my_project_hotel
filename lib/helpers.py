# lib/helpers.py
from models.hotel import Hotel
from models.client import Client
from models.employee import Employee


def exit_program():
    print("Thank you for using our system.Goodbye!")
    exit()

#Clients data
def create_client():
    name = input("Enter the client's name: ")
    address = input("Enter the client's address: ")
    needs = input("Enter the client's needs: ")
    hotel_id = input("Enter the client's hotel id: ")
    try:
        client = Client.create(name, address, needs, hotel_id)
        print(f'Successfully added: {client}')
    except Exception as exc:
        print("Error creating client: ", exc)

def list_clients():
    clients = Client.get_all()
    for client in clients:
        print(client)

def find_client_by_name():
    name = input("Enter the client's name: ")
    client = Client.find_by_name(name)
    print(client) if client else print(
        f'Client {name} not found')
    
def find_client_by_id():
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    print(client) if client else print(f'Client {id_} not found')

def update_client():
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        try:
            name = input("Enter the client's new name: ")
            client.name = name
            address = input("Enter the client's new address: ")
            client.address = address
            needs = input("Enter the client's new needs: ")
            client.needs = needs
            hotel_id = input("Enter the client's new hotel id: ")
            client.hotel_id = hotel_id

            client.update()
            print(f'Successfully updated: {client}')
        except Exception as exc:
            print("Error updating client: ", exc)
    else:
        print(f'Client {id_} not found')

def delete_client():
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        client.delete()
        print(f'Client {id_} deleted')
    else:
        print(f'Client {id_} not found')

#Employees data
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found')

def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')

def create_employee():
    name = input("Enter the employee's name: ")
    duty_assigned = input("Enter the employee's address: ")
    hotel_id = input("Enter the employee's hotel id: ")
    try:
        employee = Employee.create(name, duty_assigned, hotel_id)
        print(f'Successfully added: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)

def update_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            duty_assigned = input("Enter the employee's new duty assigned: ")
            employee.duty_assigned = duty_assigned
            hotel_id = input("Enter the employee's new hotel id: ")
            employee.hotel_id = hotel_id

            employee.update()
            print(f'Successfully updated: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')

def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


#Hotel data
def list_hotels():
    hotels = Hotel.get_all()
    for hotel in hotels:
        print(hotel)

def find_hotel_by_name():
    name = input("Enter the hotel's name: ")
    hotel = Hotel.find_by_name(name)
    print(hotel) if hotel else print(
        f'Hotel {name} not found')
    
def find_hotel_by_id():
    id_ = input("Enter the hotel's id: ")
    hotel = Hotel.find_by_id(id_)
    print(hotel) if hotel else print(f'Hotel {id_} not found')

def create_hotel():
    name = input("Enter the hotel's name: ")
    location = input("Enter the hotel's address: ")
    contact = input("Enter the hotel's contact: ")
    try:
        hotel = Hotel.create(name, location, contact)
        print(f'Successfully added: {hotel}')
    except Exception as exc:
        print("Error creating hotel: ", exc)

def update_hotel():
    id_ = input("Enter the hotel's id: ")
    if hotel := Hotel.find_by_id(id_):
        try:
            name = input("Enter the hotel's new name: ")
            hotel.name = name
            location = input("Enter the new hotel's location: ")
            hotel.location = location
            contact = input("Enter the hotel's new contact: ")
            hotel.contact = contact

            hotel.update()
            print(f'Successfully updated: {hotel}')
        except Exception as exc:
            print("Error updating hotel: ", exc)
    else:
        print(f'Hotel {id_} not found')

def delete_hotel():
    id_ = input("Enter the hotel's id: ")
    if hotel := Hotel.find_by_id(id_):
        hotel.delete()
        print(f'Hotel {id_} deleted')
    else:
        print(f'Hotel {id_} not found')

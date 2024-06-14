# lib/helpers.py
from models.hotel import Hotel
from models.client import Client
from models.employee import Employee


def exit_program():
    print("Thank you for using our system.Goodbye!")
    exit()

# def list_hotels():
#     hotels = Hotel.get_all()
#     for hotel in hotels:
#         print(hotel)

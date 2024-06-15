#!/usr/bin/env python3
# lib/cli.py

import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
from helpers import (
    enter_program,
    exit_program,
    create_client,
    list_clients,
    find_client_by_name,
    find_client_by_id,
    update_client,
    delete_client,
    list_hotel_clients,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_hotel_employees,
    list_hotels,
    find_hotel_by_name,
    find_hotel_by_id,
    create_hotel,
    update_hotel,
    delete_hotel
    
)


def main():
    enter_program()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_client()
        elif choice == "2":
            list_clients()
        elif choice == "3":
            find_client_by_name()
        elif choice == "4":
            find_client_by_id()
        elif choice == "5":
            update_client()
        elif choice == "6":
            delete_client()
        elif choice == "7":
            list_hotel_clients()
        elif choice == "8":
            list_employees()
        elif choice == "9":
            find_employee_by_name()
        elif choice == "10":
            find_employee_by_id()
        elif choice == "11":
            create_employee()
        elif choice == "12":
            update_employee()
        elif choice == "13":
            delete_employee()
        elif choice == "14":
            list_hotel_employees()
        elif choice == "15":
            list_hotels()
        elif choice == "16":
            find_hotel_by_name()
        elif choice == "17":
            find_hotel_by_id()
        elif choice == "18":
            create_hotel()
        elif choice == "19":
            update_hotel()
        elif choice == "20":
            delete_hotel()
        else:
            print(Fore.RED + "Invalid choice")


def menu():
    print(Fore.BLUE + "Please select an option:")
    print(Fore.LIGHTCYAN_EX + "0. Exit the program")
    print(Fore.LIGHTCYAN_EX + "1. Create new client")
    print(Fore.LIGHTCYAN_EX + "2. List existing clients")
    print(Fore.LIGHTCYAN_EX + "3. Find existing client by name")
    print(Fore.LIGHTCYAN_EX + "4. Find existing client by id")
    print(Fore.LIGHTCYAN_EX + "5. Update existing client's details")
    print(Fore.LIGHTCYAN_EX + "6. Delete a client")
    print(Fore.LIGHTCYAN_EX + "7. List clients in a hotel")
    print(Fore.LIGHTCYAN_EX + "8. List all employees")
    print(Fore.LIGHTCYAN_EX + "9. Find employee by name")
    print(Fore.LIGHTCYAN_EX + "10. Find employee by id")
    print(Fore.LIGHTCYAN_EX + "11. Create a new employee")
    print(Fore.LIGHTCYAN_EX + "12. Update existing employee's details")
    print(Fore.LIGHTCYAN_EX + "13. Delete an employee")
    print(Fore.LIGHTCYAN_EX + "14. List employees in a hotel")
    print(Fore.LIGHTCYAN_EX + "15. List all hotels")
    print(Fore.LIGHTCYAN_EX + "16. Find hotel by name")
    print(Fore.LIGHTCYAN_EX + "17. Find hotel by id")
    print(Fore.LIGHTCYAN_EX + "18. Create a new hotel")
    print(Fore.LIGHTCYAN_EX + "19. Update an existing hotel")
    print(Fore.LIGHTCYAN_EX + "20. Delete a hotel")
    



if __name__ == "__main__":
    main()

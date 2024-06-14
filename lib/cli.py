#!/usr/bin/env python3
# lib/cli.py

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
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new client")
    print("2. List existing clients")
    print("3. Find existing client by name")
    print("4. Find existing client by id")
    print("5. Update existing client's details")
    print("6. Delete a client")
    print("7. List clients in a hotel")
    print("8. List all employees")
    print("9. Find employee by name")
    print("10. Find employee by id")
    print("11. Create a new employee")
    print("12. Update existing employee's details")
    print("13. Delete an employee")
    print("14. List employees in a hotel")
    print("15. List all hotels")
    print("16. Find hotel by name")
    print("17. Find hotel by id")
    print("18. Create a new hotel")
    print("19. Update an existing hotel")
    print("20. Delete a hotel")
    



if __name__ == "__main__":
    main()

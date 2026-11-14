
"""Main entry point for the Smart Parking Management System."""

from parking import (
    register_vehicle,
    get_available_spaces,
    get_parked_vehicles,
    get_parking_fee,
)
from payments import process_payment

def display_menu():
    """Display the available parking management options."""
    print("\n" + "=" * 45)
    print("      SMART PARKING MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Register vehicle entry")
    print("2. Check parking fee")
    print("3. Process parking payment")
    print("4. Validate vehicle exit")
    print("5. Check parking availability")
    print("6. View daily report")
    print("7. View parked vehicles")
    print("0. Exit")
    print("=" * 45)


def main():
    """Run the application's main menu."""
    while True:
        display_menu()

        choice = input("Select an option: ").strip()

        if choice == "0":
            print("\nThank you for using Smart Parking!")
            break

        
        elif choice == "1":
            license_plate = input("Enter license plate: ")
            result = register_vehicle(license_plate)
            print(f"\n{result}")

        
        elif choice == "2":
            ticket_id = input("Enter ticket ID: ")
            result = get_parking_fee(ticket_id)
            print(f"\n{result}")

        elif choice == "3":
            ticket_id = input("Enter ticket ID for payment: ")
            result = process_payment(ticket_id)
            print(f"\n{result}")

        elif choice == "5":
            available = get_available_spaces()
            print(f"\nAvailable parking spaces: {available}")

        elif choice == "7":
            report = get_parked_vehicles()
            print(f"\n{report}")

        elif choice in ("4", "6"):
            print(f"\nOption {choice} is not available yet.")

        else:
            print("\nInvalid option. Please try again.")



if __name__ == "__main__":
    main()

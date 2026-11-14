
"""Main entry point for the Smart Parking Management System."""

from parking import (
    register_vehicle,
    get_available_spaces,
    get_parked_vehicles,
    get_parking_fee,
)

def display_menu():
    """Display the available parking management options."""
    print("\n" + "=" * 45)
    print("      SMART PARKING MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Register vehicle entry")
    print("2. Check parking fee")
    print("3. Validate vehicle exit")
    print("4. Check parking availability")
    print("5. View daily report")
    print("6. View parked vehicles")
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

        elif choice == "4":
            available = get_available_spaces()
            print(f"\nAvailable parking spaces: {available}")

        elif choice == "6":
            report = get_parked_vehicles()
            print(f"\n{report}")    

        elif choice in ("3", "5"):
            print(f"\nOption {choice} is not available yet.")


        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()

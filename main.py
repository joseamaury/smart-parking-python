
"""Main entry point for the Smart Parking Management System."""


def display_menu():
    """Display the available parking management options."""
    print("\n" + "=" * 45)
    print("      SMART PARKING MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Register vehicle entry")
    print("2. Process parking payment")
    print("3. Validate vehicle exit")
    print("4. Check parking availability")
    print("5. View daily report")
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

        elif choice in ("1", "2", "3", "4", "5"):
            print(f"\nOption {choice} is not available yet.")

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()

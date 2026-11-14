
"""Vehicle registration and parking management operations."""

from datetime import datetime, timezone
from pricing import calculate_parking_fee

# Temporary storage for registered vehicles
parked_vehicles = []

# Maximum number of available parking spaces
PARKING_CAPACITY = 30

# Sequential ticket counter
ticket_counter = 0


def register_vehicle(license_plate):
    """Register a vehicle and generate its parking ticket."""

    global ticket_counter

    license_plate = license_plate.strip().upper()

    if not license_plate:
        return "Error: License plate cannot be empty."

    if len(parked_vehicles) >= PARKING_CAPACITY:
        return "Error: Parking facility is full."

    for vehicle in parked_vehicles:
        if vehicle["license_plate"] == license_plate:
            return "Error: Vehicle is already registered."

    ticket_counter += 1

    ticket_id = f"TKT-{ticket_counter:04d}"
    entry_time = datetime.now(timezone.utc)

    vehicle = {
        "ticket_id": ticket_id,
        "license_plate": license_plate,
        "entry_time": entry_time,
        "status": "PARKED",
        "payment_status": "UNPAID"
    }

    parked_vehicles.append(vehicle)

    return (
        "\n========== PARKING TICKET ==========\n"
        f"Ticket ID: {ticket_id}\n"
        f"License Plate: {license_plate}\n"
        f"Entry Time (UTC): {entry_time:%d/%m/%Y %H:%M:%S}\n"
        f"Status: {vehicle['status']}\n"
        f"Payment: {vehicle['payment_status']}\n"
        "===================================="
    )



def get_available_spaces():
    """Return the number of available parking spaces."""

    return PARKING_CAPACITY - len(parked_vehicles)



def get_parked_vehicles():
    """Return a list of vehicles currently parked."""

    if not parked_vehicles:
        return "There are no vehicles currently parked."

    report = "\n========== PARKED VEHICLES ==========\n"

    for vehicle in parked_vehicles:
        report += (
            f"\nTicket ID: {vehicle['ticket_id']}\n"
            f"License Plate: {vehicle['license_plate']}\n"
            f"Entry Time (UTC): "
            f"{vehicle['entry_time']:%d/%m/%Y %H:%M:%S}\n"
            f"Status: {vehicle['status']}\n"
            f"Payment: {vehicle['payment_status']}\n"
            "-------------------------------------\n"
        )

    report += f"\nTotal parked vehicles: {len(parked_vehicles)}"

    return report




def get_parking_fee(ticket_id):
    """Calculate the parking fee and display the payment status."""

    ticket_id = ticket_id.strip().upper()

    for vehicle in parked_vehicles:
        if vehicle["ticket_id"] == ticket_id:

            result = calculate_parking_fee(
                vehicle["entry_time"]
            )

            if isinstance(result, str):
                return result

            payment_status = vehicle.get("payment_status", "UNPAID")

            return (
                "\n========== PARKING FEE ==========\n"
                f"Ticket ID: {ticket_id}\n"
                f"License Plate: {vehicle['license_plate']}\n"
                f"Charged Hours: {result['charged_hours']}\n"
                f"Total Fee: €{result['total_fee']:.2f}\n"
                f"Payment Status: {payment_status}\n"
                "================================="
            )

    return "Error: Ticket not found."


def validate_vehicle_exit(ticket_id):
    """Validate payment and release the parking space."""

    ticket_id = ticket_id.strip().upper()

    for vehicle in parked_vehicles:
        if vehicle["ticket_id"] == ticket_id:

            if vehicle["payment_status"] != "PAID":
                return "Error: Payment required before exit."

            exit_time = datetime.now(timezone.utc)

            vehicle["status"] = "EXITED"
            vehicle["exit_time"] = exit_time

            parked_vehicles.remove(vehicle)

            return (
                "\n========== EXIT RECEIPT ==========\n"
                f"Ticket ID: {ticket_id}\n"
                f"License Plate: {vehicle['license_plate']}\n"
                f"Exit Time (UTC): {exit_time:%d/%m/%Y %H:%M:%S}\n"
                f"Status: {vehicle['status']}\n"
                "Parking space released successfully.\n"
                "=================================="
            )

    return "Error: Ticket not found."

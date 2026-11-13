
"""Vehicle registration and parking management operations."""

from datetime import datetime, timezone

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

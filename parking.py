
"""Vehicle registration and parking management operations."""

# Temporary storage for registered vehicles
parked_vehicles = []

# Maximum number of available parking spaces
PARKING_CAPACITY = 30


def register_vehicle(license_plate):
    """Register a vehicle entering the parking facility."""

    license_plate = license_plate.strip().upper()

    if not license_plate:
        return "Error: License plate cannot be empty."

    if len(parked_vehicles) >= PARKING_CAPACITY:
        return "Error: Parking facility is full."

    for vehicle in parked_vehicles:
        if vehicle["license_plate"] == license_plate:
            return "Error: Vehicle is already registered."

    vehicle = {
        "license_plate": license_plate,
        "status": "PARKED"
    }

    parked_vehicles.append(vehicle)

    return f"Vehicle {license_plate} registered successfully!"


def get_available_spaces():
    """Return the number of available parking spaces."""

    return PARKING_CAPACITY - len(parked_vehicles)

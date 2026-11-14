
"""Simulated parking payment operations."""

from datetime import datetime, timezone

from parking import parked_vehicles
from pricing import calculate_parking_fee


def process_payment(ticket_id):
    """Process a simulated payment for a parking ticket."""

    ticket_id = ticket_id.strip().upper()

    for vehicle in parked_vehicles:

        if vehicle["ticket_id"] == ticket_id:

            if vehicle["payment_status"] == "PAID":
                return "Error: This ticket has already been paid."

            result = calculate_parking_fee(
                vehicle["entry_time"]
            )

            if isinstance(result, str):
                return result

            total_fee = result["total_fee"]

            vehicle["payment_status"] = "PAID"
            vehicle["payment_time"] = datetime.now(timezone.utc)
            vehicle["amount_paid"] = total_fee

            return (
                "\n========== PAYMENT RECEIPT ==========\n"
                f"Ticket ID: {ticket_id}\n"
                f"License Plate: {vehicle['license_plate']}\n"
                f"Charged Hours: {result['charged_hours']}\n"
                f"Amount Paid: €{total_fee:.2f}\n"
                f"Payment Time (UTC): "
                f"{vehicle['payment_time']:%d/%m/%Y %H:%M:%S}\n"
                f"Payment Status: {vehicle['payment_status']}\n"
                "====================================="
            )

    return "Error: Ticket not found."


"""Parking duration and pricing calculations."""

from datetime import datetime, timezone
from math import ceil

# Parking rate in euros per hour
HOURLY_RATE = 4.00


def calculate_parking_fee(entry_time, exit_time=None):
    """Calculate parking duration and total parking fee."""

    if exit_time is None:
        exit_time = datetime.now(timezone.utc)

    duration = exit_time - entry_time

    total_seconds = duration.total_seconds()

    if total_seconds < 0:
        return "Error: Exit time cannot be before entry time."

    total_hours = total_seconds / 3600

    charged_hours = max(1, ceil(total_hours))

    total_fee = charged_hours * HOURLY_RATE

    return {
        "duration": duration,
        "charged_hours": charged_hours,
        "total_fee": total_fee
    }

# Smart Parking Management System

A Python-based command-line application designed to simulate the daily operations of a private parking facility in Dublin, Ireland.

This project is being developed as part of my Python learning journey, focusing on practical programming skills, modular development, and real-world problem-solving.

## Project Status

**In Development**

The application is being built incrementally, with new features, improvements, and documentation added throughout the development process.

## Current Features

- Vehicle registration using license plates
- Automatic parking ticket generation
- Unique sequential ticket IDs during each application session
- Parking capacity management (30 spaces)
- Parking duration and fee calculation
- Hourly parking rate of €4.00
- Automatic rounding up to the next full hour
- Simulated parking payments
- Payment status tracking (PAID / UNPAID)
- Vehicle exit validation
- Parking space release after vehicle exit
- List of currently parked vehicles
- Input validation and basic error handling
- UTC timestamps for parking operations

## Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub
- Python standard library

## Project Structure

```text
smart-parking-python/
├── main.py        # Main application and interactive menu
├── parking.py     # Vehicle registration and parking management
├── pricing.py     # Parking fee calculations
├── payments.py    # Simulated payment processing
├── README.md      # Project documentation
└── .gitignore     # Git exclusions
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/joseamaury/smart-parking-python.git
```

2. Navigate to the project directory:

```bash
cd smart-parking-python
```

3. Run the application:

```bash
python main.py
```

Python 3 is required. No external packages are currently needed.

## Parking Rules

- Maximum parking capacity: 30 vehicles.
- Parking fee: €4.00 per hour.
- Partial hours are rounded up to a full hour.
- Each registered vehicle receives a ticket.
- Payments are simulated; no real financial transactions are processed.
- Vehicles must have a PAID status before leaving.
- Parking spaces become available again after vehicle exit.

## Planned Improvements

- Persistent data storage
- Logging and improved error handling
- Daily reports and CSV export
- Automated unit tests
- Additional documentation and code improvements

## Current Limitations

- Data is stored in memory and is lost when the application closes.
- Ticket numbering resets when the application restarts.
- Payments are simulated and do not connect to a payment provider.

## Author

**José Amaury Machado Junior**

GitHub: [joseamaury](https://github.com/joseamaury)

This project is part of my professional development and transition into the technology industry.
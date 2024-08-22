import datetime

# Sample data for EV charging stations
charging_stations = [
    {"id": 1, "name": "Green Energy Charging", "location": "Downtown", "fast_charging": True, "available_slots": 5, 
     "time_slots": {"09:00 AM": "available", "10:00 AM": "available", "11:00 AM": "available"}},
    {"id": 2, "name": "EcoCharge", "location": "Uptown", "fast_charging": False, "available_slots": 3, 
     "time_slots": {"09:00 AM": "available", "10:00 AM": "available", "11:00 AM": "available"}},
    {"id": 3, "name": "QuickCharge Hub", "location": "Suburb", "fast_charging": True, "available_slots": 7, 
     "time_slots": {"09:00 AM": "available", "10:00 AM": "available", "11:00 AM": "available"}},
    {"id": 4, "name": "Solar Power Station", "location": "Midtown", "fast_charging": False, "available_slots": 4, 
     "time_slots": {"09:00 AM": "available", "10:00 AM": "available", "11:00 AM": "available"}},
]

# Store booked appointments
appointments = []

def filter_stations(location=None, fast_charging=None):
    filtered_stations = charging_stations
    if location:
        filtered_stations = [station for station in filtered_stations if station["location"].lower() == location.lower()]
    if fast_charging is not None:
        filtered_stations = [station for station in filtered_stations if station["fast_charging"] == fast_charging]
    return filtered_stations

def display_stations(stations):
    if not stations:
        print("No stations found matching your criteria.")
    else:
        print("Available Charging Stations:")
        for station in stations:
            print(f"ID: {station['id']}, Name: {station['name']}, Location: {station['location']}, "
                  f"Fast Charging: {'Yes' if station['fast_charging'] else 'No'}, "
                  f"Available Slots: {station['available_slots']}")

def display_time_slots(station):
    print(f"\nAvailable Time Slots for {station['name']}:")
    for time, status in station["time_slots"].items():
        if status == "available":
            print(f"{time}")

def book_slot(station_id, user_name, booking_date, selected_time):
    station = next((s for s in charging_stations if s["id"] == station_id), None)
    if station:
        if station["time_slots"].get(selected_time) == "available":
            station["time_slots"][selected_time] = "booked"
            station["available_slots"] -= 1
            appointment = {
                "user": user_name,
                "station_id": station_id,
                "station_name": station["name"],
                "date": booking_date,
                "time": selected_time,
                "status": "to-do"
            }
            appointments.append(appointment)
            print(f"Slot booked successfully at {station['name']} on {booking_date} at {selected_time}")
        else:
            print("The selected time slot is not available.")
    else:
        print("Invalid station ID.")

def update_appointment():
    print("\nYour Current Appointments:")
    for i, appointment in enumerate(appointments):
        print(f"{i+1}. {appointment['station_name']} on {appointment['date']} at {appointment['time']} - Status: {appointment['status']}")
    
    if not appointments:
        print("No appointments to update.")
        return

    appt_number = int(input("Enter the number of the appointment to update: ")) - 1
    if 0 <= appt_number < len(appointments):
        appointments[appt_number]["status"] = "done"
        station_id = appointments[appt_number]["station_id"]
        selected_time = appointments[appt_number]["time"]

        # Update slot availability
        station = next((s for s in charging_stations if s["id"] == station_id), None)
        if station:
            station["time_slots"][selected_time] = "available"
            station["available_slots"] += 1
        print("Appointment status updated to 'done'.")
    else:
        print("Invalid appointment number.")

def main():
    while True:
        print("\nEV Charging Station Finder and Slot Booking")
        print("1. Find Charging Stations")
        print("2. Book a Slot")
        print("3. Update Appointment")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            location = input("Enter location (or leave blank to skip): ")
            fast_charging_input = input("Require fast charging? (yes/no): ").lower()
            fast_charging = True if fast_charging_input == 'yes' else False if fast_charging_input == 'no' else None

            stations = filter_stations(location, fast_charging)
            display_stations(stations)

        elif choice == '2':
            station_id = int(input("Enter the ID of the station to book a slot: "))
            user_name = input("Enter your name: ")
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            station = next((s for s in charging_stations if s["id"] == station_id), None)

            if station:
                display_time_slots(station)
                selected_time = input("Enter the time slot you want to book (e.g., 09:00 AM): ")
                book_slot(station_id, user_name, booking_date, selected_time)
            else:
                print("Invalid station ID.")

        elif choice == '3':
            update_appointment()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

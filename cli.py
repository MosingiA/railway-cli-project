import random
from db import get_session
from models.init import init_db
from models.station import Station
from models.train import Train
from models.passenger import Passenger
from models.base import Base, Session

session = get_session()

# ---------- Helpers ----------
def simulate_payment(amount, phone):
    print(f"📲 Sending STK Push for KES {amount} to {phone}...")
    confirm = input("Confirm payment? (y/n): ").strip().lower()
    if confirm == "y":
        print("✅ Payment successful!")
        return True
    else:
        print("❌ Payment cancelled.")
        return False


# ---------- CRUD ----------
def add_station():
    name = input("Enter station name: ")
    location = input("Enter station location: ")
    station = Station(name=name, location=location)
    session.add(station)
    session.commit()
    print(f"✅ Station '{name}' added.")


def view_stations():
    stations = session.query(Station).all()
    if not stations:
        print("⚠️ No stations found.")
    for s in stations:
        print(s)


def add_train():
    name = input("Enter train name: ")
    destination = input("Enter train destination: ")

    view_stations()
    station_id = int(input("Enter station ID for this train: "))

    train = Train(name=name, destination=destination, station_id=station_id)
    session.add(train)
    session.commit()
    print(f"✅ Train '{name}' added.")


def view_trains():
    trains = session.query(Train).all()
    if not trains:
        print("⚠️ No trains found.")
    for t in trains:
        print(t)


def add_passenger():
    name = input("Enter passenger name: ")
    destination = input("Enter passenger destination: ")
    # phone = input("Enter passenger phone: ")

    # Show available trains
    view_trains()
    train_id = int(input("Enter train ID to book: "))

    # Generate random ticket number
    ticket_number = f"TKT{random.randint(1000,9999)}"

    # ✅ Save passenger first (always added to DB)
    passenger = Passenger(
        name=name,
        destination=destination,
        # phone=phone,
        ticket_number=ticket_number,
        train_id=train_id,
    )
    session.add(passenger)
    session.commit()
    print(f"✅ Passenger {name} added successfully with Ticket {ticket_number}.")

    # ✅ Ask for payment after saving
    print("Payment options: 1. Phone   2. Cash  3. Skip")
    pay_choice = input("Choose payment method: ").strip()

    if pay_choice == "1":
        simulate_payment(200, phone)
    elif pay_choice == "2":
        print(f"💵 Cash payment accepted for {name}.")
    else:
        print("⚠ Passenger added without payment.")



def view_passengers():
    passengers = session.query(Passenger).all()
    if not passengers:
        print("⚠️ No passengers found.")
    for p in passengers:
        print(p)


# ---------- Main Menu ----------
def main_menu():
    while True:
        print("\n Railway Station CLI ")
        print("1. Add Station")
        print("2. View Stations")
        print("3. Add Train")
        print("4. View Trains")
        print("5. Add Passenger")
        print("6. View Passengers")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_station()
        elif choice == "2":
            view_stations()
        elif choice == "3":
            add_train()
        elif choice == "4":
            view_trains()
        elif choice == "5":
            add_passenger()
        elif choice == "6":
            view_passengers()
        elif choice == "0":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice.")


if __name__ == "__main__":
    main_menu()

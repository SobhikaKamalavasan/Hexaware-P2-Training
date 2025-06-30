from dao.CarLeaseRepositoryImpl import CarLeaseRepositoryImpl 
from entity.Car import Car
from entity.Customer import Customer
from datetime import datetime
import sys

STATUS_AVAILABLE = 'available'
STATUS_NOT_AVAILABLE = 'notAvailable'
repo = CarLeaseRepositoryImpl()

def get_date_input(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt + " (YYYY-MM-DD): "), "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid date format. Please enter in YYYY-MM-DD.")

while True:
    print("\n--- CAR RENTAL SYSTEM ---")
    print("1. Add Car")
    print("2. Add Customer")
    print("3. Create Lease")
    print("4. List Available Cars")
    print("5. Find Car by ID")
    print("6. List All Customers")
    print("7. Find Customer by ID")
    print("8. Exit")
    
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("❌ Invalid input. Enter a number.")
        continue

    if choice == 1:
        print("\n--- Add Car ---")
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = int(input("Enter year: "))
        rate = float(input("Enter daily rate: "))
        status = input("Enter status (available / notAvailable): ").strip()
        passenger_capacity = int(input("Enter passenger capacity: "))
        engine_capacity = float(input("Enter engine capacity (in cc): "))

        car = Car(None, make, model, year, rate, status, passenger_capacity, engine_capacity)
        repo.addCar(car)
        print("✅ Car added.")

    elif choice == 2:
        print("\n--- Add Customer ---")
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        customer = Customer(None, fname, lname, email, phone)
        repo.addCustomer(customer)
        print("✅ Customer added.")

    elif choice == 3:
        print("\n--- Create Lease ---")
        try:
            cust_id = int(input("Enter customer ID: "))
            car_id = int(input("Enter car ID: "))
            start_date = get_date_input("Enter start date")
            end_date = get_date_input("Enter end date")

            lease = repo.createLease(cust_id, car_id, start_date, end_date)
            print("✅ Lease created:", lease.__dict__)
        except Exception as e:
            print(f"❌ Failed to create lease: {e}")

    elif choice == 4:
        print("\n--- Available Cars ---")
        try:
            cars = repo.listAvailableCars()
            if cars:
                for car in cars:
                    print(car)
            else:
                print("No cars available.")
        except Exception as e:
            print(f"❌ Error fetching available cars: {e}")

    elif choice == 5:
        print("\n--- Find Car by ID ---")
        try:
            car_id = int(input("Enter Car ID: "))
            car = repo.findCarById(car_id)
            print("Car Found:", car)
        except Exception as e:
            print(f"❌ {e}")

    elif choice == 6:
        print("\n--- All Customers ---")
        try:
            customers = repo.listCustomers()
            if customers:
                for cust in customers:
                    print(cust)
            else:
                print("No customers found.")
        except Exception as e:
            print(f"❌ Error fetching customers: {e}")

    elif choice == 7:
        print("\n--- Find Customer by ID ---")
        try:
            cust_id = int(input("Enter Customer ID: "))
            customer = repo.findCustomerById(cust_id)
            print("Customer Found:", customer)
        except Exception as e:
            print(f"❌ {e}")

    elif choice == 8:
        print("👋 Exiting... Goodbye!")
        sys.exit()

    else:
        print("❌ Invalid choice. Try again.")

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.carleaserepository_impl import CarLeaseRepositoryImpl
from myexceptions.car_not_found_exception import CarNotFoundException
from myexceptions.lease_not_found_exception import LeaseNotFoundException
from myexceptions.customer_not_found_exception import CustomerNotFoundException

def main():
    repo = CarLeaseRepositoryImpl()

    try:
        car_id = int(input("Enter Car ID to search: "))
        car = repo.findCarById(car_id)
        print(f"Car Found: {car.get_make()} {car.get_model()}")

    except CarNotFoundException as e:
        print(f"[Error] {e}")

    try:
        customer_id = int(input("Enter Customer ID to search: "))
        customer = repo.findCustomerById(customer_id)
        print(f"Customer Found: {customer.get_firstName()} {customer.get_lastName()}")

    except CustomerNotFoundException as e:
        print(f"[Error] {e}")

    try:
        lease_id = int(input("Enter Lease ID to return car: "))
        lease = repo.returnCar(lease_id)
        print(f"Returned Vehicle for Lease ID: {lease_id}")

    except LeaseNotFoundException as e:
        print(f"[Error] {e}")

if __name__ == '__main__':
    main()

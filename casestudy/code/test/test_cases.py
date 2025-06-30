import unittest
from datetime import date
from dao.CarLeaseRepositoryImpl import CarLeaseRepositoryImpl
from entity.Car import Car
from entity.Customer import Customer
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException

STATUS_AVAILABLE = 1
STATUS_NOT_AVAILABLE = 0
class TestCarRentalSystem(unittest.TestCase):

    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()
    

    def test_add_car(self):
        car = Car(None, "TestMake", "TestModel", 2024, 3000, STATUS_AVAILABLE, 5, 1500)
        self.repo.addCar(car)
        cars = self.repo.listAvailableCars()
        #print("Available cars:",cars)
        self.assertTrue(any(c[1] == "TestMake" for c in cars))  

    def test_create_lease(self):
        lease = self.repo.createLease(1, 1, date(2025, 6, 21), date(2025, 6, 25))
        self.assertIsNotNone(lease)
        self.assertEqual(lease.carID, 1)
        self.assertEqual(lease.customerID, 1)

    def test_list_active_leases(self):
        leases = self.repo.listActiveLeases()
        self.assertIsInstance(leases, list)
        self.assertTrue(len(leases) >= 0)


    def test_find_car_not_found_exception(self):
        with self.assertRaises(CarNotFoundException):
            self.repo.findCarById(99999)

    def test_find_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            self.repo.findCustomerById(99999)

    def test_return_car_lease_not_found_exception(self):
        with self.assertRaises(LeaseNotFoundException):
            self.repo.returnCar(99999)

if __name__ == '__main__':
    unittest.main()

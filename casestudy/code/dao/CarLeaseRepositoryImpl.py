from dao.ICarLeaseRepository import ICarLeaseRepository
from util.DBConnUtil import getConnection
from entity.Car import Car
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Payment import Payment
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException
from datetime import date
STATUS_AVAILABLE = 1
STATUS_NOT_AVAILABLE = 0
class CarLeaseRepositoryImpl(ICarLeaseRepository):

    def __init__(self):
        self.conn = getConnection()
        self.cursor = self.conn.cursor()

    # ---------------- CAR MANAGEMENT ----------------

    def addCar(self, car):
        sql = "INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (car.make, car.model, car.year, car.dailyRate, car.status, car.passengerCapacity, car.engineCapacity)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def removeCar(self, carID):
        self.cursor.execute("DELETE FROM Vehicle WHERE vehicleID = %s", (carID,))
        self.conn.commit()

    def listAvailableCars(self):
        self.cursor.execute("SELECT * FROM Vehicle WHERE status = 1")
        #self.cursor.execute("SELECT * FROM Vehicle WHERE status = 'available'")
        return self.cursor.fetchall()

    def listRentedCars(self):
        self.cursor.execute("SELECT * FROM Vehicle WHERE status = 0")
        return self.cursor.fetchall()

    def findCarById(self, carID):
        self.cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = %s", (carID,))
        result = self.cursor.fetchone()
        if not result:
            raise CarNotFoundException("Car ID not found!")
        return result

    # ---------------- CUSTOMER MANAGEMENT ----------------

    def addCustomer(self, customer):
        sql = "INSERT INTO Customer (firstName, lastName, email, phoneNumber) VALUES (%s, %s, %s, %s)"
        val = (customer.firstName, customer.lastName, customer.email, customer.phoneNumber)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def removeCustomer(self, customerID):
        self.cursor.execute("DELETE FROM Customer WHERE customerID = %s", (customerID,))
        self.conn.commit()

    def listCustomers(self):
        self.cursor.execute("SELECT * FROM Customer")
        return self.cursor.fetchall()

    def findCustomerById(self, customerID):
        self.cursor.execute("SELECT * FROM Customer WHERE customerID = %s", (customerID,))
        result = self.cursor.fetchone()
        if not result:
            raise CustomerNotFoundException("Customer ID not found!")
        return result

    # ---------------- LEASE MANAGEMENT ----------------

    def createLease(self, customerID, carID, startDate, endDate):
        self.findCustomerById(customerID)
        self.findCarById(carID)
        sql = "INSERT INTO lease (carID, customerID, startDate, endDate, leaseType) VALUES (%s, %s, %s, %s, %s)"
        val = (carID, customerID, startDate, endDate, "Daily")
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.cursor.execute("UPDATE vehicle SET status=%s WHERE vehicleID = %s", (STATUS_NOT_AVAILABLE, carID))

        #self.cursor.execute("UPDATE Vehicle SET status='notAvailable' WHERE vehicleID = %s", (carID,))
        self.conn.commit()

        self.cursor.execute("SELECT * FROM Lease ORDER BY leaseID DESC LIMIT 1")
        result = self.cursor.fetchone()
        return Lease(*result)

    def returnCar(self, leaseID):
        self.cursor.execute("SELECT * FROM Lease WHERE leaseID = %s", (leaseID,))
        lease = self.cursor.fetchone()
        if not lease:
            raise LeaseNotFoundException("Lease ID not found!")

        self.cursor.execute("UPDATE vehicle SET status=%s WHERE vehicleID = %s", (STATUS_AVAILABLE, lease[1]))

        #self.cursor.execute("UPDATE Vehicle SET status='available' WHERE vehicleID = %s", (lease[1],))
        self.conn.commit()
        return Lease(*lease)

    def listActiveLeases(self):
        today = date.today()
        self.cursor.execute("SELECT * FROM Lease WHERE endDate > %s", (today,))
        return self.cursor.fetchall()

    def listLeaseHistory(self):
        self.cursor.execute("SELECT * FROM Lease")
        return self.cursor.fetchall()

    # ---------------- PAYMENT HANDLING ----------------

    def recordPayment(self, leaseID, amount):
        today = date.today()
        sql = "INSERT INTO Payment (leaseID, paymentDate, amount) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (leaseID, today, amount))
        self.conn.commit()

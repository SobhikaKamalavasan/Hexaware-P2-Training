from dao.icarleaserepository import ICarLeaseRepository

class CarLeaseRepositoryImpl(ICarLeaseRepository):
    def addCar(self, car):
        print("Adding car...")

    def removeCar(self, carID):
        print("Removing car...")

    def listAvailableCars(self):
        return []

    def listRentedCars(self):
        return []

    def findCarById(self, carID):
        raise Exception("Car not found")

    def addCustomer(self, customer):
        print("Adding customer...")

    def removeCustomer(self, customerID):
        print("Removing customer...")

    def listCustomers(self):
        return []

    def findCustomerById(self, customerID):
        raise Exception("Customer not found")

    def createLease(self, customerID, carID, startDate, endDate):
        return {}

    def returnCar(self, leaseID):
        raise Exception("Lease not found")

    def listActiveLeases(self):
        return []

    def listLeaseHistory(self):
        return []

    def recordPayment(self, lease, amount):
        print("Recording payment...")

from abc import ABC, abstractmethod

class ICarLeaseRepository(ABC):
    @abstractmethod
    def addCar(self, car): pass
    @abstractmethod
    def removeCar(self, carID): pass
    @abstractmethod
    def listAvailableCars(self): pass
    @abstractmethod
    def listRentedCars(self): pass
    @abstractmethod
    def findCarById(self, carID): pass
    @abstractmethod
    def addCustomer(self, customer): pass
    @abstractmethod
    def removeCustomer(self, customerID): pass
    @abstractmethod
    def listCustomers(self): pass
    @abstractmethod
    def findCustomerById(self, customerID): pass
    @abstractmethod
    def createLease(self, customerID, carID, startDate, endDate): pass
    @abstractmethod
    def returnCar(self, leaseID): pass
    @abstractmethod
    def listActiveLeases(self): pass
    @abstractmethod
    def listLeaseHistory(self): pass
    @abstractmethod
    def recordPayment(self, lease, amount): pass


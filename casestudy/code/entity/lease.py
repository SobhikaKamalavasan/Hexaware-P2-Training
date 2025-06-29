
class Lease:
    def __init__(self, leaseID, vehicleID, customerID, startDate, endDate, leaseType):
        self.__leaseID = leaseID
        self.__vehicleID = vehicleID
        self.__customerID = customerID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__leaseType = leaseType

    def get_leaseID(self): return self.__leaseID
    def get_vehicleID(self): return self.__vehicleID
    def get_customerID(self): return self.__customerID
    def get_startDate(self): return self.__startDate
    def get_endDate(self): return self.__endDate
    def get_leaseType(self): return self.__leaseType

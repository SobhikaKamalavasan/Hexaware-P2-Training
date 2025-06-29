
class Vehicle:
    def __init__(self, vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity):
        self.__vehicleID = vehicleID
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__status = status
        self.__passengerCapacity = passengerCapacity
        self.__engineCapacity = engineCapacity

    def get_vehicleID(self): return self.__vehicleID
    def get_make(self): return self.__make
    def get_model(self): return self.__model
    def get_year(self): return self.__year
    def get_dailyRate(self): return self.__dailyRate
    def get_status(self): return self.__status
    def get_passengerCapacity(self): return self.__passengerCapacity
    def get_engineCapacity(self): return self.__engineCapacity

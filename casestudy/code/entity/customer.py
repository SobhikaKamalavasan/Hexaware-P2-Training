
class Customer:
    def __init__(self, customerID, firstName, lastName, email, phoneNumber):
        self.__customerID = customerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber

    def get_customerID(self): return self.__customerID
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_email(self): return self.__email
    def get_phoneNumber(self): return self.__phoneNumber

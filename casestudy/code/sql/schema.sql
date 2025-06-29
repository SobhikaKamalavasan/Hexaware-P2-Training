
CREATE DATABASE IF NOT EXISTS car_rental;
USE car_rental;

CREATE TABLE IF NOT EXISTS Vehicle (
    vehicleID INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(100),
    model VARCHAR(100),
    year INT,
    dailyRate DECIMAL(10,2),
    status ENUM('available', 'notAvailable'),
    passengerCapacity INT,
    engineCapacity FLOAT
);

CREATE TABLE IF NOT EXISTS Customer (
    customerID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(100),
    lastName VARCHAR(100),
    email VARCHAR(100),
    phoneNumber VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Lease (
    leaseID INT AUTO_INCREMENT PRIMARY KEY,
    vehicleID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    type VARCHAR(20),
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE IF NOT EXISTS Payment (
    paymentID INT AUTO_INCREMENT PRIMARY KEY,
    leaseID INT,
    paymentDate DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID)
);

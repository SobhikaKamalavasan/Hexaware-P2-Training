
-- Car Rental System - SQL Schema

-- 1. Vehicle Table
CREATE TABLE vehicle (
    vehicleID INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    dailyRate DECIMAL(10,2) NOT NULL,
    status INT NOT NULL,  -- 1 = available, 0 = not available
    passengerCapacity INT NOT NULL,
    engineCapacity INT NOT NULL
);

-- 2. Customer Table
CREATE TABLE customer (
    customerID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phoneNumber VARCHAR(15)
);

-- 3. Lease Table
CREATE TABLE lease (
    leaseID INT AUTO_INCREMENT PRIMARY KEY,
    carID INT,
    customerID INT,
    startDate DATE,
    endDate DATE,
    leaseType VARCHAR(20),
    FOREIGN KEY (carID) REFERENCES vehicle(vehicleID),
    FOREIGN KEY (customerID) REFERENCES customer(customerID)
);

-- 4. Payment Table
CREATE TABLE payment (
    paymentID INT AUTO_INCREMENT PRIMARY KEY,
    leaseID INT,
    paymentDate DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (leaseID) REFERENCES lease(leaseID)
);

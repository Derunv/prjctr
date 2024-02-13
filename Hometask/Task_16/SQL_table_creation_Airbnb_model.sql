CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_type VARCHAR(10) NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);


CREATE TABLE Rooms (
    room_id INT PRIMARY KEY,
    host_id INT,
    capacity INT,
    price_per_night DECIMAL(10, 2),
    has_ac BOOLEAN,
    has_refrigerator BOOLEAN,
    FOREIGN KEY (host_id) REFERENCES Users(user_id)
);


CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in_date DATE,
    check_out_date DATE,
    FOREIGN KEY (guest_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);


CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    guest_id INT,
    host_id INT,
    room_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (guest_id) REFERENCES Users(user_id),
    FOREIGN KEY (host_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);


CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    amount_paid DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (guest_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

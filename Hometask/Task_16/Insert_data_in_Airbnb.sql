INSERT INTO Users (user_id, user_type, name, email, password)
VALUES
    (1, 'Host', 'Alice Host', 'alice@example.com', 'password123'),
    (2, 'Guest', 'Bob Guest', 'bob@example.com', 'password456'),
    (3, 'Host', 'Charlie Host', 'charlie@example.com', 'password789');


INSERT INTO Rooms (room_id, host_id, capacity, price_per_night, has_ac, has_refrigerator)
VALUES
    (1, 1, 2, 50.00, true, true),
    (2, 1, 4, 100.00, false, true),
    (3, 1, 3, 75.00, true, false);

INSERT INTO Reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date)
VALUES
    (1, 2, 1, '2024-02-10', '2024-02-15'),
    (2, 2, 2, '2024-03-05', '2024-03-10'),
    (3, 1, 3, '2024-04-20', '2024-04-25');

INSERT INTO Reviews (review_id, guest_id, host_id, room_id, rating, comment)
VALUES
    (1, 2, 1, 1, 5, 'Great host and comfortable room!'),
    (2, 2, 1, 2, 4, 'Nice room but could use better Wi-Fi signal'),
    (3, 1, 2, 3, 5, 'Amazing stay, everything was perfect!');

INSERT INTO Payments (payment_id, guest_id, room_id, amount_paid, payment_date)
VALUES
    (1, 2, 1, 250.00, '2024-02-09'),
    (2, 2, 2, 500.00, '2024-03-01'),
    (3, 1, 3, 450.00, '2024-04-18');

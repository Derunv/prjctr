SELECT name, user_id
FROM Users
WHERE user_id = (
    SELECT guest_id
    FROM Reservations
    GROUP BY guest_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
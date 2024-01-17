-- Assuming you have a table named 'students'
-- Create the need_meeting view

DELIMITER //

CREATE FUNCTION SafeDiv (
a INT,
b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END //

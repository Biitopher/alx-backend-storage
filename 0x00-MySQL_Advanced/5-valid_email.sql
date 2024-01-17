-- Assuming you have a table named 'users'
-- Create a trigger to reset 'valid_email' when 'email' is updated

DELIMITER //
CREATE TRIGGER reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER;

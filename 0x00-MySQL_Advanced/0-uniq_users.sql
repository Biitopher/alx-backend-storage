-- Check if the table already exists before creating
-- Create the users table
    CREATE TABLE IF NOT EXIST users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,       
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
    );

-- Check if the table already exists before creating
-- Create the users table
    CREATE IF NOT EXIST TABLE users (
        id INT IDENTITY(1,1) PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
    );

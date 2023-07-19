-- Create the second_table in the hbtn_0c_0 database
-- If the table already exists, the script will not fail

USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Add multiple rows to the second_table
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);

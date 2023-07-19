-- Update the score of Bob to 10 in the second_table
-- without using Bob's id value
-- (only using the name field)

USE hbtn_0c_0;

UPDATE second_table
SET score = 10
WHERE name = 'Bob';

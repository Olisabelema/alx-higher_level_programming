-- List all records with a score >= 10 in the second_table
-- of the database hbtn_0c_0. Displaying both the score and the name,
-- and ordering by score (top first)

USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

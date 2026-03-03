-- Script that lists all records of the table second_table of the database on a MySQL server
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != "" 
ORDER BY score DESC;
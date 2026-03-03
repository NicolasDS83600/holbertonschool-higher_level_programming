-- Script that lists all records with a score >= 10 in second_table of a database on a MySQL server
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
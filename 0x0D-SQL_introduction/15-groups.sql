-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Getting same score
USE hbtn_0c_0;
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC, score;

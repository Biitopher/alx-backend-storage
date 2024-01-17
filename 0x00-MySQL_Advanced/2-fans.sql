-- Assuming you have already imported the metal_bands table
-- Create a temporary table to store the rankings

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;

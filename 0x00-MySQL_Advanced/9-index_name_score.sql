-- Assuming you have a table named 'names' with columns 'name' and 'score'
-- Create the idx_name_first_score index on the first letter of the 'name' column and 'score'
CREATE INDEX idx_name_first_score ON names(name(1), score);


-- Assuming you have a table named 'names'
-- Create the idx_name_first index on the first letter of the 'name' column

CREATE INDEX idx_name_first ON names(name(1));

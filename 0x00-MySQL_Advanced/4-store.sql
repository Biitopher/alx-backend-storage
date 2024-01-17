-- Assuming you have tables named 'orders' and 'items'
-- Create trigger to update the quantity in 'items' table after  new order

CREATE TRIGGER decrement
AFTER INSERT
ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;

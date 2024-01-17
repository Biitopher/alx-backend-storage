-- Assuming you have already imported the metal_bands table
-- Calculate the lifespan for each band with Glam rock as the main style

SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;

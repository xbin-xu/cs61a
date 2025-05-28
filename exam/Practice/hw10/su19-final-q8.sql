-- 8. (10 points) The Big SQL
-- The ingredients table describes the dish and part for each part of each dish
-- at a restaurant. The shops table describes the food, shop, and price for
-- each part of a dish sold at each of two shops. All ingredients (parts) are
-- sold by both shops, and each ingredient will only appear once for each shop.
-- Write your SQL statements so that they would still be correct if table
-- contents changed. You can assume the shops table will only ever contain two
-- shops (A and B).

CREATE TABLE ingredients AS
    SELECT "chili" AS dish, "beans" AS part UNION
    SELECT "chili",         "onions"        UNION
    SELECT "soup",          "broth"         UNION
    SELECT "soup",          "onions"        UNION
    SELECT "beans",         "beans";

CREATE TABLE shops AS
    SELECT "beans" AS food, "A" AS shop, 2 AS price UNION
    SELECT "beans",         "B",         2 AS price UNION
    SELECT "onions",        "A",         3          UNION
    SELECT "onions",        "B",         2          UNION
    SELECT "broth",         "A",         3          UNION
    SELECT "broth",         "B",         5;


-- (a) (2 pt) Select a two-column table with one row per food that describes
-- the lowest price for each food.
-- +--------+---+
-- | beans  | 2 |
-- | broth  | 3 |
-- | onions | 2 |
-- +--------+---+
SELECT food, MIN(price) FROM shops GROUP BY food;


-- (b) (4 pt) Select a two-column table with one row per dish that describes
-- the total cost of each dish if all parts are purchased from shop A.
-- +-------+---+
-- | beans | 2 |
-- | chili | 5 |
-- | soup  | 6 |
-- +-------+---+
-- SELECT dish, SUM(price) AS cost FROM ingredients, shops
--     WHERE part = food AND shop = "A" GROUP BY dish ORDER BY cost;
-- Official Solution
SELECT dish, SUM(price) FROM ingredients, shops
    WHERE part = food AND shop = "A" GROUP BY dish ORDER BY dish;


-- (c) (4 pt) In two different ways, select a one-column table of all foods
-- that have a different price at each store.
-- +--------+
-- | onions |
-- | broth  |
-- +--------+
-- SELECT a.food FROM shops AS a, shops AS b
--     WHERE a.food = b.food AND a.shop < b.shop AND a.price != b.price;
-- SELECT food FROM shops GROUP BY food HAVING COUNT(DISTINCT price) > 1;
-- Official Solution
SELECT a.food FROM shops AS a, shops AS b
    WHERE a.food = b.food AND a.price > b.price;
SELECT food FROM shops GROUP BY food HAVING MAX(price) > MIN(price);

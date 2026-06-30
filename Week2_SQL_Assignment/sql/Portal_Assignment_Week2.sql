/* DROP TABLE IF EXISTS superstore;

CREATE TABLE superstore (
    "Row ID" TEXT,
    "Order ID" TEXT,
    "Order Date" TEXT,
    "Ship Date" TEXT,
    "Ship Mode" TEXT,
    "Customer ID" TEXT,
    "Customer Name" TEXT,
    "Segment" TEXT,
    "Country" TEXT,
    "City" TEXT,
    "State" TEXT,
    "Postal Code" TEXT,
    "Region" TEXT,
    "Product ID" TEXT,
    "Category" TEXT,
    "Sub-Category" TEXT,
    "Product Name" TEXT,
    "Sales" TEXT,
    "Quantity" TEXT,
    "Discount" TEXT,
    "Profit" TEXT
);

/*ALTER TABLE superstore
ALTER COLUMN "Row ID" TYPE BIGINT
USING "Row ID"::BIGINT;

ALTER TABLE superstore
ALTER COLUMN "Postal Code" TYPE BIGINT
USING "Postal Code"::BIGINT;

ALTER TABLE superstore
ALTER COLUMN "Sales" TYPE DECIMAL(10,2)
USING "Sales"::DECIMAL;


ALTER TABLE superstore
ALTER COLUMN "Quantity" TYPE INT
USING "Quantity"::INT;


ALTER TABLE superstore
ALTER COLUMN "Discount" TYPE DECIMAL(5,2)
USING "Discount"::DECIMAL;

ALTER TABLE superstore
ALTER COLUMN "Profit" TYPE DECIMAL(10,2)
USING "Profit"::DECIMAL;


ALTER TABLE superstore
ALTER COLUMN "Order Date" TYPE DATE
USING TO_DATE("Order Date", 'MM-DD-YYYY');

ALTER TABLE superstore
ALTER COLUMN "Ship Date" TYPE DATE
USING TO_DATE("Ship Date", 'MM-DD-YYYY');

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'superstore';

*/

SELECT *
FROM superstore
WHERE "Region" = 'West';

SELECT *
FROM superstore
WHERE "Category" = 'Technology';

SELECT *
FROM superstore
WHERE "Sales" > 500;

SELECT *
FROM superstore
WHERE "Order Date"
BETWEEN '2017-01-01' AND '2017-12-31';

SELECT *
FROM superstore
WHERE "Category" = 'Technology'
AND "Region" = 'West'
AND "Sales" > 500;

SELECT
    "Category",
    SUM("Sales") AS total_sales
FROM superstore
GROUP BY "Category"
ORDER BY total_sales DESC;

SELECT
    "Region",
    AVG("Profit") AS average_profit
FROM superstore
GROUP BY "Region"
ORDER BY average_profit DESC;


SELECT
    "Category",
    SUM("Quantity") AS total_quantity_sold
FROM superstore
GROUP BY "Category"
ORDER BY total_quantity_sold DESC;

SELECT
    "Region",
    COUNT(*) AS total_orders
FROM superstore
GROUP BY "Region"
ORDER BY total_orders DESC;

SELECT
    "Category",
    AVG("Discount") AS average_discount
FROM superstore
GROUP BY "Category"
ORDER BY average_discount DESC;

SELECT
    "Product Name",
    "Sales"
FROM superstore
ORDER BY "Sales" DESC
LIMIT 10;

SELECT
    "Category",
    SUM("Profit") AS total_profit
FROM superstore
GROUP BY "Category"
ORDER BY total_profit DESC;

SELECT
    DATE_TRUNC('month', "Order Date") AS month,
    SUM("Sales") AS monthly_sales
FROM superstore
GROUP BY month

SELECT
    "Customer Name",
    SUM("Sales") AS total_sales
FROM superstore
GROUP BY "Customer Name"
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    "Order ID",
    COUNT(*)
FROM superstore
GROUP BY "Order ID"
HAVING COUNT(*) > 1;


SELECT COUNT(*)
FROM superstore;

*/

SELECT
    COUNT(*) FILTER (WHERE "Sales" IS NULL) AS missing_sales,
    COUNT(*) FILTER (WHERE "Profit" IS NULL) AS missing_profit
FROM superstore;

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;



CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name TEXT,
    segment TEXT
);


INSERT INTO customers (customer_id, customer_name, segment)

SELECT DISTINCT
    "Customer ID",
    "Customer Name",
    "Segment"
FROM superstore_raw;



CREATE TABLE products (
    product_id VARCHAR(50),
    product_name TEXT,
    category TEXT,
    sub_category TEXT
);

INSERT INTO products (product_id, product_name, category, sub_category)

SELECT DISTINCT
    "Product ID",
    "Product Name",
    "Category",
    "Sub-Category"
FROM superstore_raw;


CREATE TABLE orders (
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    customer_id VARCHAR(50),
    sales NUMERIC(10,2),
    quantity INTEGER,
    profit NUMERIC(10,2),
    region TEXT,
    state TEXT
);


INSERT INTO orders (
    order_id,
    order_date,
    ship_date,
    customer_id,
    sales,
    quantity,
    profit,
    region,
    state
)

SELECT DISTINCT
    "Order ID",
    "Order Date",
    "Ship Date",
    "Customer ID",
    "Sales",
    "Quantity",
    "Profit",
    "Region",
    "State"
FROM superstore_raw;
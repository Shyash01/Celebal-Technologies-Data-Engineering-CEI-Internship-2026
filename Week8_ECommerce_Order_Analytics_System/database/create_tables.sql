-- ==========================================
-- Customers Table
-- ==========================================

CREATE TABLE customers (

    customer_id VARCHAR(10) PRIMARY KEY,
   customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    registration_date DATE NOT NULL,
    customer_type VARCHAR(20) NOT NULL
        CHECK (customer_type IN ('REGULAR', 'PREMIUM', 'VIP'))
);

-- ==========================================
-- Products Table
-- ==========================================

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50) NOT NULL,
    cost_price NUMERIC(10,2) NOT NULL
        CHECK (cost_price >= 0)

);

-- ==========================================
-- Orders Table
-- ==========================================

CREATE TABLE orders (

    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    order_date TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL
        CHECK (status IN ('DELIVERED','PLACED','CANCELLED', 'SHIPPED','RETURNED')),

    region_code VARCHAR(10) NOT NULL,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- ==========================================
-- Order Items Table
-- ==========================================

CREATE TABLE order_items (
    item_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    quantity INTEGER NOT NULL
        CHECK (quantity <> 0),

    unit_price NUMERIC(10,2) NOT NULL
        CHECK (unit_price >= 0),

    discount_percent INTEGER NOT NULL
        CHECK (discount_percent BETWEEN 0 AND 100),
    CONSTRAINT fk_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)

);
/* SELECT
    orders.order_id,
    orders.order_date,
    customers.first_name,
    customers.last_name,
    orders.total_amount
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;

SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    orders.order_id,
    orders.total_amount
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id; */
SELECT
    orders.order_id,
    products.product_name,
    order_items.quantity,
    order_items.unit_price,
    order_items.discount_pct
FROM orders
JOIN order_items
ON orders.order_id = order_items.order_id
JOIN products
ON order_items.product_id = products.product_id;
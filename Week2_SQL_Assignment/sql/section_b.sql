/* SELECT *
FROM orders
WHERE status = 'Delivered';


SELECT *
FROM products
WHERE category = 'Electronics'
AND unit_price > 2000;


SELECT *
FROM customers
WHERE state = 'Maharashtra'
AND join_date BETWEEN '2024-01-01' AND '2024-12-31'; 

SELECT *
FROM orders
WHERE order_date BETWEEN '2024-08-10' AND '2024-08-25'
AND status != 'Cancelled'; 

SELECT *
FROM orders
WHERE order_date BETWEEN '2024-08-01' AND '2024-08-31'; */

SELECT *
FROM customers
WHERE join_date BETWEEN '2024-01-01' AND '2024-12-31';
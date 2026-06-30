/* SELECT COUNT(*) AS total_orders
FROM orders; 

SELECT
    SUM(total_amount) AS total_revenue
FROM orders
WHERE status = 'Delivered';

SELECT
    category,
    AVG(unit_price) AS average_price
FROM products
GROUP BY category;


SELECT
    status,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY status
ORDER BY total_revenue DESC;
SELECT
    category,
    MAX(unit_price) AS highest_price,
    MIN(unit_price) AS lowest_price
FROM products
GROUP BY category;

SELECT
    category,
    AVG(unit_price) AS average_price
FROM products
GROUP BY category
HAVING AVG(unit_price) > 2000;

*/

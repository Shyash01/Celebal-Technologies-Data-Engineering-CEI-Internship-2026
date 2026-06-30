--Query 1
-- Total Revenue Per Category  (revenue = quantity × unit_price × (1 - discount_percent/100)) 

SELECT p.category,
    SUM(
        oi.quantity * oi.unit_price * (1- oi.discount_percent /100.00)
    ) AS total_revenue

FROM order_items oi
JOIN products p ON oi.product_id = p.product_id

GROUP BY p.category
ORDER BY total_revenue


-- Query 2
-- Top 10 customers by total order value 

SELECT

    c.customer_id,
    c.customer_name,

    SUM(
        oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
    ) AS total_order_value

FROM customers c

JOIN orders o ON c.customer_id = o.customer_id

JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY     c.customer_id, c.customer_name
ORDER BY total_order_value DESC
LIMIT 10;


-- Query 3
-- Month-wise order count for the last 12 months
-- Query 3
-- Month-wise order count for the last 12 months

SELECT
    DATE_TRUNC('month', order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders

WHERE order_date >= (
    SELECT MAX(order_date) - INTERVAL '12 months'
    FROM orders
)

GROUP BY month
ORDER BY month;

/* Note: WE CAN USE FROM THE CURRENT DATE ALSO, BUT SINCE THE DATABASE NOT GETTING UPDATED TIMELY SO I AM USING LATEST ORDER DATE FOR SUBQUERRY AS WE STUDIED DURING WEEK 3
SELECT
    DATE_TRUNC('month', order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '12 months'
GROUP BY month
ORDER BY month;
*/


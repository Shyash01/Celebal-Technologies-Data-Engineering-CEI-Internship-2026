
-- Query 1
-- Top 5 Customers by Total Sales

/*
SELECT
    customer_id,
    SUM(sales) AS total_sales

FROM orders

GROUP BY customer_id

ORDER BY total_sales DESC

LIMIT 5;


-- Query 2
-- Bottom 5 Customers by Total Sales

SELECT
    customer_id,
    SUM(sales) AS total_sales

FROM orders

GROUP BY customer_id

ORDER BY total_sales ASC

LIMIT 5;

-- Query 3
-- Customers with Only One Order


SELECT
    customer_id,
    COUNT(order_id) AS total_orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id) = 1;


-- Query 4
-- Customers with Above Average Sales


WITH customer_sales AS (

    SELECT
        customer_id,
        SUM(sales) AS total_sales

    FROM orders

    GROUP BY customer_id

)

SELECT *
FROM customer_sales

WHERE total_sales > (

    SELECT AVG(total_sales)
    FROM customer_sales

)

ORDER BY total_sales DESC;
*/


-- Query 5
-- Highest Order Value Per Customer


SELECT
    customer_id,
    MAX(sales) AS highest_order_value

FROM orders

GROUP BY customer_id

ORDER BY highest_order_value DESC;

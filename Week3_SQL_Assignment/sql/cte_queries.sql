
-- Query 1
-- Total Sales for Each Customer Using CTE
/*
WITH customer_sales AS (

    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id

)

SELECT *
FROM customer_sales
ORDER BY total_sales DESC;
*/


-- Query 2
-- Customers with Above Average Total Sales
								
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
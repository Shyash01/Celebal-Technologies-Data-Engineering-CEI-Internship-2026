
-- Query 1
-- Rank Customers Based on Total Sales
/*

WITH customer_sales AS (

    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id

)

SELECT
    customer_id,
    total_sales,

    RANK() OVER (
        ORDER BY total_sales DESC
    ) AS sales_rank

FROM customer_sales;

-- Query 2
-- Row Numbers for Orders Within Each Customer


SELECT
    customer_id,
    order_id,
    sales,

    ROW_NUMBER() OVER (

        PARTITION BY customer_id
        ORDER BY sales DESC

    ) AS row_number

FROM orders;
*/
-- ============================================
-- Query 3
-- Top 3 Customers Based on Total Sales
-- ============================================

WITH customer_sales AS (

    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id

),

customer_rank AS (

    SELECT
        customer_id,
        total_sales,

        RANK() OVER (
            ORDER BY total_sales DESC
        ) AS sales_rank

    FROM customer_sales

)

SELECT *
FROM customer_rank
WHERE sales_rank <= 3;
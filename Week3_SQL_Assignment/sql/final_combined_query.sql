
-- Final Combined Query
-- JOIN + CTE + Window Function

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

SELECT
    c.customer_name,
    cr.total_sales,
    cr.sales_rank

FROM customer_rank cr

JOIN customers c
ON cr.customer_id = c.customer_id

ORDER BY cr.sales_rank;
-- Query 7
-- Calculate running total of revenue per region, ordered by date

-- Although this could be writtne as a single nestde query, i am using a samll CTE which makes it much easeir to read
-- As using the appraoach that first calcualte the daily reveneu and then calculate the running total/ 

WITH daily_revenue AS (
    SELECT
        o.region_code,
        o.order_date,
        SUM(
            oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
        ) AS daily_revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY
        o.region_code,
        o.order_date
)

SELECT
    region_code,
    order_date,
    ROUND(daily_revenue, 2) AS daily_revenue,
    ROUND(
        SUM(daily_revenue) OVER (
            PARTITION BY region_code
            ORDER BY order_date
        ), 2
    ) AS running_total
FROM daily_revenue
ORDER BY
    region_code,
    order_date;

-- Query 8
-- Ranking with DENSE_RANK :  For each category, rank products by total revenue

WITH product_revenue AS (
    SELECT p.category,
        p.product_name,
        
        SUM(
            oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
    ) AS total_revenue

    FROM products p
    
    JOIN order_items oi ON p.product_id = oi.product_id
    
    GROUP BY p.category,
        p.product_name
)

SELECT category, product_name,
    
    ROUND(total_revenue, 2) AS total_revenue,
    
    DENSE_RANK() OVER (
        PARTITION BY category
        ORDER BY total_revenue DESC
    ) AS rank_in_category

FROM product_revenue

ORDER BY category, rank_in_category, product_name;


-- Query 9
-- Calculate days between consecutive orders using LAG()
WITH customer_orders AS (
    SELECT
        customer_id,
        order_date,
        LAG(order_date) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
),

order_gaps AS (
    SELECT
        customer_id,
        order_date,
        previous_order_date,
        ROUND(
            EXTRACT(EPOCH FROM (order_date - previous_order_date)) / 86400,
            2
        ) AS days_gap
    FROM customer_orders
    WHERE previous_order_date IS NOT NULL
),

customer_status AS (
    SELECT
        customer_id,
        AVG(days_gap) AS average_gap
    FROM order_gaps
    GROUP BY customer_id
)

SELECT
    og.customer_id,
    og.order_date,
    og.previous_order_date,
    og.days_gap,
    CASE
        WHEN cs.average_gap > 30 THEN 'At Risk'
        ELSE 'Active'
    END AS customer_status
FROM order_gaps og
JOIN customer_status cs
    ON og.customer_id = cs.customer_id
ORDER BY cs.average_gap,
    og.customer_id,
    og.order_date;

-- Query 10
-- Monthly customer revenue categorization using multiple CTEs

WITH monthly_revenue AS (
    SELECT
        o.customer_id,
        DATE_TRUNC('month', o.order_date) AS order_month,
        SUM(
            oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
        ) AS monthly_revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY
        o.customer_id,
        DATE_TRUNC('month', o.order_date)
),

customer_category AS (
    SELECT
        customer_id,
        order_month,
        monthly_revenue,
        CASE
            WHEN monthly_revenue > 10000 THEN 'High'
            WHEN monthly_revenue BETWEEN 5000 AND 10000 THEN 'Medium'
            ELSE 'Low'
        END AS revenue_category
    FROM monthly_revenue
)

SELECT
    order_month,
    revenue_category,
    COUNT(customer_id) AS total_customers
FROM customer_category
GROUP BY
    order_month,
    revenue_category
ORDER BY
    order_month,
    revenue_category;

-- Query 11
-- Divide customers into 4 quartiles based on total lifetime revenue
-- Query 11
-- Divide customers into 4 quartiles based on total lifetime revenue

WITH customer_revenue AS (
    SELECT
        o.customer_id,
        SUM(
            oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
        ) AS total_value
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY o.customer_id
),

customer_segments AS (
    SELECT
        customer_id,
        total_value,
        NTILE(4) OVER (
            ORDER BY total_value DESC
        ) AS quartile
    FROM customer_revenue
)

SELECT
    customer_id,
    ROUND(total_value, 2) AS total_value,
    quartile,
    CASE
        WHEN quartile = 1 THEN 'Platinum'
        WHEN quartile = 2 THEN 'Gold'
        WHEN quartile = 3 THEN 'Silver'
        ELSE 'Bronze'
    END AS quartile_label
FROM customer_segments
ORDER BY total_value DESC;


-- Query 12
-- Compare each month's revenue with the same month of the previous year

WITH monthly_revenue AS (
    SELECT
        EXTRACT(YEAR FROM o.order_date) AS year,
        EXTRACT(MONTH FROM o.order_date) AS month,
        SUM(
            oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
        ) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY
        EXTRACT(YEAR FROM o.order_date),
        EXTRACT(MONTH FROM o.order_date)
)

SELECT
    year,
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(
        LAG(revenue) OVER (
            PARTITION BY month
            ORDER BY year
        ),
        2
    ) AS previous_year_revenue,
    ROUND(
        (
            (revenue - LAG(revenue) OVER (
                PARTITION BY month
                ORDER BY year
            ))
            /
            LAG(revenue) OVER (
                PARTITION BY month
                ORDER BY year
            )
        ) * 100,
        2
    ) AS yoy_growth_percent
FROM monthly_revenue
ORDER BY
    year,
    month;


-- Query 13
-- Display first and latest order date for each customer

SELECT DISTINCT
    customer_id,

    FIRST_VALUE(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS first_order_date,

    LAST_VALUE(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND UNBOUNDED FOLLOWING
    ) AS latest_order_date

FROM orders
ORDER BY customer_id;

-- Query 14
-- Calculate cumulative distribution based on customer revenue
-- Query 14
-- Calculate cumulative revenue contribution of customers

WITH customer_revenue AS (
    SELECT
        o.customer_id,
        SUM(
            oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)
        ) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY o.customer_id
),

cumulative_revenue AS (
    SELECT
        customer_id,
        revenue,

        SUM(revenue) OVER (
            ORDER BY revenue DESC
        ) AS cumulative_revenue,

        SUM(revenue) OVER () AS total_revenue

    FROM customer_revenue
)

SELECT
    customer_id,
    ROUND(revenue, 2) AS revenue,
    ROUND(cumulative_revenue, 2) AS cumulative_revenue,
    ROUND(
        (cumulative_revenue * 100.0 / total_revenue),
        2
    ) AS cumulative_percent
FROM cumulative_revenue
ORDER BY revenue DESC;

-- Query 15
-- Cohort Analysis with Retention Rate

WITH customer_cohort AS (

    SELECT
        customer_id,
        DATE_TRUNC('month', registration_date) AS cohort_month
    FROM customers

),

customer_orders AS (

    SELECT
        cc.customer_id,
        cc.cohort_month,
        DATE_TRUNC('month', o.order_date) AS order_month,

        (
            EXTRACT(YEAR FROM AGE(DATE_TRUNC('month', o.order_date), cc.cohort_month)) * 12
            +
            EXTRACT(MONTH FROM AGE(DATE_TRUNC('month', o.order_date), cc.cohort_month))
        ) AS month_number

    FROM customer_cohort cc
    JOIN orders o
        ON cc.customer_id = o.customer_id

),

cohort_summary AS (

    SELECT

        cohort_month,

        COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END) AS month_0,

        COUNT(DISTINCT CASE WHEN month_number = 1 THEN customer_id END) AS month_1,

        COUNT(DISTINCT CASE WHEN month_number = 2 THEN customer_id END) AS month_2,

        COUNT(DISTINCT CASE WHEN month_number = 3 THEN customer_id END) AS month_3

    FROM customer_orders

    GROUP BY cohort_month

)

SELECT

    cohort_month,

    month_0,

    month_1,

    month_2,

    month_3,

    ROUND(month_1 * 100.0 / NULLIF(month_0,0),2) AS retention_month_1,

    ROUND(month_2 * 100.0 / NULLIF(month_0,0),2) AS retention_month_2,

    ROUND(month_3 * 100.0 / NULLIF(month_0,0),2) AS retention_month_3

FROM cohort_summary

ORDER BY cohort_month;
-- Query 16
-- Find products frequently bought together


WITH product_pairs AS (

    SELECT

        p1.product_name AS product_a,

        p2.product_name AS product_b,

        COUNT(*) AS times_bought_together

    FROM order_items oi1

    JOIN order_items oi2

        ON oi1.order_id = oi2.order_id
       AND oi1.product_id < oi2.product_id

    JOIN products p1

        ON oi1.product_id = p1.product_id

    JOIN products p2

        ON oi2.product_id = p2.product_id

    GROUP BY

        p1.product_name,
        p2.product_name

)

SELECT

    product_a,

    product_b,

    times_bought_together,

    ROW_NUMBER() OVER(

        ORDER BY times_bought_together DESC

    ) AS pair_rank

FROM product_pairs

ORDER BY

    pair_rank;
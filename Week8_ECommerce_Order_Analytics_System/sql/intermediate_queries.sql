-- Query 4
-- Customers who placed orders but never had any item delivered

SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders -- Has placed an order
)
AND customer_id NOT IN (
    SELECT customer_id FROM orders WHERE status = 'DELIVERED' -- But never had a delivery
);
-- Query 5
-- Products with more returns than purchases

SELECT p.product_id, p.product_name,
    SUM(
        CASE 
            WHEN oi.quantity > 0 THEN oi.quantity 
            ELSE 0 
            END
        ) AS purchased,
    ABS(SUM(
        CASE 
            WHEN oi.quantity < 0 THEN oi.quantity 
            ELSE 0 
            END
            )
        ) AS returned

FROM products p

JOIN order_items oi ON p.product_id = oi.product_id

GROUP BY p.product_id, p.product_name
HAVING SUM(oi.quantity) < 0;

-- Query 6
-- Calculate the return rate (returned items / total items) per category 

SELECT p.category,
    COUNT(
        CASE
            WHEN o.status = 'RETURNED' THEN 1
        END
    ) AS returned_items,

    COUNT(*) AS total_items,

    ROUND(
        COUNT(
            CASE
                WHEN o.status = 'RETURNED' THEN 1
            END
        ) * 100.0 / COUNT(*), 2
    ) AS return_rate

FROM order_items oi

JOIN orders o
ON oi.order_id = o.order_id

JOIN products p
ON oi.product_id = p.product_id

GROUP BY p.category
ORDER BY return_rate DESC;
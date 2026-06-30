
-- Query 1
-- Orders with Sales Greater Than Average Sales

/*
SELECT
    order_id,
    customer_id,
    sales
FROM orders
WHERE sales > (
    SELECT AVG(sales)
    FROM orders
);



-- Query 2
-- Highest Sales Order for Each Customer


SELECT
    customer_id,
    order_id,
    sales
FROM orders o1
WHERE sales = (
    SELECT MAX(sales)
    FROM orders o2
    WHERE o1.customer_id = o2.customer_id
)
ORDER BY sales DESC;
*/
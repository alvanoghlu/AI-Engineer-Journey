
-- =========================================
-- WEEK 2 SQL PRACTICAL TEST
-- =========================================


-- 1. Calculate the total order amount for each customer
SELECT
    customer,
    SUM(amount) AS total_amount
FROM orders
GROUP BY customer
ORDER BY total_amount DESC;


-- 2. Find the largest order(s), including ties
SELECT
    customer,
    amount,
    created_at
FROM orders
WHERE amount = (
    SELECT MAX(amount)
    FROM orders
);


-- 3. Calculate the total order amount for each month
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(amount) AS monthly_total
FROM orders
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month ASC;


-- 4. Rank customers by their total order amount
WITH customer_totals AS (
    SELECT
        customer,
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer
)
SELECT
    customer,
    total_amount,
    RANK() OVER (
        ORDER BY total_amount DESC
    ) AS customer_rank
FROM customer_totals
ORDER BY customer_rank;


-- 5. Find customers with at least two orders
SELECT
    customer,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer
HAVING COUNT(*) >= 2
ORDER BY order_count DESC;


-- 6. Find orders above the average order amount
WITH average_order AS (
    SELECT AVG(amount) AS avg_amount
    FROM orders
)
SELECT
    o.customer,
    o.amount,
    o.created_at
FROM orders o
CROSS JOIN average_order a
WHERE o.amount > a.avg_amount
ORDER BY o.amount DESC;
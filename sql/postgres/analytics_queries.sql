-- KPI 1 : Total Revenue

SELECT
    ROUND(SUM(payment_value), 2) AS total_revenue
FROM raw.payments;


-- KPI 2 : Total Orders

SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM raw.orders;


-- KPI 3 : Average Order Value (AOV)

SELECT
    ROUND(
        SUM(payment_value) /
        COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM raw.payments;
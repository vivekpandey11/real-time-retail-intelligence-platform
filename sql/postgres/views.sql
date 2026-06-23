CREATE OR REPLACE VIEW analytics.vw_sales_summary AS

SELECT
    order_id,
    customer_state,
    revenue,
    order_date
FROM analytics.fct_sales;
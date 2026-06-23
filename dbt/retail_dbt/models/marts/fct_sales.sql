SELECT
    o.order_id,
    c.customer_state,
    p.payment_value AS revenue,
    DATE(o.order_purchase_timestamp) AS order_date

FROM {{ ref('stg_orders') }} o

JOIN {{ ref('stg_customers') }} c
    ON o.customer_id = c.customer_id

JOIN {{ ref('stg_payments') }} p
    ON o.order_id = p.order_id
/*
STAR SCHEMA DESIGN

FACT TABLE
-----------
fct_sales
- order_id
- customer_id
- revenue
- order_date

DIMENSIONS
-----------
dim_customers
- customer_id
- customer_city
- customer_state

dim_products
- product_id
- product_category_name

RELATIONSHIPS
-------------
dim_customers.customer_id
        |
        |
fct_sales.customer_id

dim_products.product_id
        |
        |
fct_sales.product_id
*/
-- 17-join.sql
SELECT * FROM sales;
SELECT * FROM customers;

SELECT
    *,
    (
        SELECT customer_name FROM customers as
        WHERE customers.customer_id=sales.customer_id
    )
FROM sales;
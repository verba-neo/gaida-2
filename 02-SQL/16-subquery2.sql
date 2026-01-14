-- 16-subquery2.sql
/*
Scala  -> 데이터 1개 | 14.56
Vector -> 데이터 1줄 | ("인천", "대구", "부산", "광주", "서울")
Matrix -> 행*열
*/

-- Scala
SELECT AVG(total_amount) FROM sales;
-- Vector
SELECT DISTINCT region from sales;

-- VIP들의 주문내역만 확인
SELECT customer_id FROM customers WHERE customer_type='VIP';

SELECT * FROM sales 
WHERE customer_id 
IN (SELECT customer_id FROM customers WHERE customer_type='VIP');




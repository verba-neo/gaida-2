-- 12-aggr-func.sql (집계함수)
-- id,order_date,customer_id,product_id,product_name,category,quantity,unit_price,total_amount,sales_rep,region

SELECT * FROM sales;

-- COUNT
SELECT 
    COUNT(*) AS 매출건수
FROM sales;

SELECT
    COUNT(*) AS 총주문건수,
    COUNT(DISTINCT customer_id) AS 고객수,
    COUNT(DISTINCT product_name) AS 상품수
FROM sales;

-- SUM
SELECT
    SUM(total_amount) AS 총매출액,
    SUM(quantity) AS 총판매수량,
    TO_CHAR(SUM(total_amount), 'FM999,999,999') || '원' AS -- 천단위,찍기
FROM sales;

-- '서울' 발생 매출 총합
SELECT
    SUM(total_amount) AS 총매출,
    COUNT(*) AS 주문건수
FROM sales
WHERE region='서울';

-- AVG(평균)
SELECT
    AVG(total_amount) AS 회당평균주문액,
    AVG(quantity) AS 평균구매수량,
    ROUND(AVG(unit_price)) AS 평균단가
FROM sales;

-- MIN/MAX
SELECT
    MIN(total_amount) AS 최소매출액,
    MAX(total_amount) AS 최대매출액,
    MIN(order_date) AS 첫주문일,
    MAX(order_date) AS 마지막주문일
FROM sales;

-- 매출 대시보드
SELECT
    COUNT(*) AS 주문건수,
    SUM(total_amount) AS 총매출,
    ROUND(AVG(total_amount)) AS 평균매출,
    MIN(total_amount) AS 최소매출액,
    MAX(total_amount) AS 최대매출액,
    ROUND(AVG(quantity), 2) AS 평균수량 -- ROUND(x, 1) -> 소숫점 1자리 반올림
FROM sales

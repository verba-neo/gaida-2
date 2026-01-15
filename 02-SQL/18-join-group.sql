-- 18-join-group.sql
-- VIP 고객(c)들의 구매 내역(s) 조회 (*)
SELECT *
FROM customers c
INNER JOIN sales s ON c.customer_id=s.customer_id
WHERE c.customer_type='VIP';

-- 각 등급별 구매액 평균 확인

SELECT
    c.customer_type AS 등급,
    COUNT(*) AS 고객수,
    ROUND(AVG(s.total_amount)) AS 평균구매액
FROM customers c
INNER JOIN sales s ON c.customer_id=s.customer_id
GROUP BY c.customer_type;

-- [모든 고객]의 고객 별 구매 현황 분석
-- 고객 이름, 고객 등급, 주문 횟수, 총구매액, 평균주문액, 최근주문일













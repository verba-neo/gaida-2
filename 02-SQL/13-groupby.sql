-- 13-groupby.sql

SELECT
    region,
	category,
    COUNT(*) AS 주문건수,
    ROUND(AVG(total_amount), 2) AS 평균매출
FROM sales
GROUP BY region, category
ORDER BY 평균매출 DESC
LIMIT 3;
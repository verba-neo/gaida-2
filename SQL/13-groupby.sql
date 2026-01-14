-- 13-groupby.sql

SELECT * FROM sales WHERE region='서울' OR region='광주';
SELECT * FROM sales WHERE region IN ('서울', '광주');
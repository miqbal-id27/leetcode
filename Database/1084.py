## 1084. Sales Analysis III
## https://leetcode.com/problems/sales-analysis-iii/description/

"""
Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table can have duplicate rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
 

Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.

The result format is in the following example.
"""

"""
SELECT
    p.product_id AS product_id,
    p.product_name AS product_name
FROM (
    SELECT
        product_id,
        product_name
    FROM Product
) AS p
    LEFT JOIN (
        SELECT
            product_id,
            sale_date
        FROM Sales
    ) AS s
    ON p.product_id = s.product_id
GROUP BY 
    product_id,
    product_name
HAVING
    MIN(s.sale_date) >= '2019-01-01'
    AND MAX(s.sale_date) <= '2019-03-31';
"""

# Optimized submission from others

"""
SELECT p.product_id, p.product_name
FROM Product p
WHERE EXISTS (
    SELECT 1
    FROM Sales s
    WHERE s.product_id = p.product_id
      AND s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
)
AND NOT EXISTS (
    SELECT 1
    FROM Sales s
    WHERE s.product_id = p.product_id
      AND (s.sale_date < '2019-01-01' OR s.sale_date > '2019-03-31')
);
"""

"""
SELECT DISTINCT p.product_id, product_name 
FROM Product p 
JOIN Sales s
ON p.product_id = s.product_id
WHERE p.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31' )
"""

"""
SELECT product_id, product_name
FROM Product
JOIN Sales USING (product_id)
GROUP BY product_id
HAVING COUNT(CASE WHEN sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31' THEN 1 END) = 0
"""

"""
with products_excl as
(select distinct product_id from Sales where sale_date < '2019-01-01' or sale_date > '2019-03-31')

select product_id, product_name
from Product
where product_id not in (select product_id from products_excl)
and product_id in (select distinct product_id from Sales)
"""
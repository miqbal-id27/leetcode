## 586. Customer Placing the Largest Number of Orders
## https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

"""
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The result format is in the following example.
"""

"""
SELECT
    customer_number
FROM
    (
    SELECT 
        customer_number AS customer_number,
        COUNT(customer_number) AS order_count
    FROM Orders
    GROUP BY customer_number
    ) AS co
ORDER BY order_count DESC
LIMIT 1;
"""

# Optimized submission from others
"""
SELECT customer_number
FROM Orders 
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;
"""


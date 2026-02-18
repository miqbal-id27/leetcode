## 610. Triangle Judgement
## https://leetcode.com/problems/triangle-judgement/description/

"""
Table: Triangle

+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
 

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
"""

"""
SELECT
    *,
    CASE 
        WHEN z < x + y AND x < z + y AND y < x + z THEN "Yes"
        ELSE "No"
    END AS triangle
FROM Triangle;
"""

# Optimized submission from others

"""

select *, if(x+y>z and y+z>x and x+z>y, "Yes","No") as triangle from triangle
"""
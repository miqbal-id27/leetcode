## 596. Classes With at Least 5 Students
## https://leetcode.com/problems/classes-with-at-least-5-students/description/

"""
Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
 

Write a solution to find all the classes that have at least five students.

Return the result table in any order.

The result format is in the following example.
"""

"""
SELECT
    cs.class AS class
FROM
    (
    SELECT 
        class AS class,
        COUNT(student) AS student_count
    FROM Courses
    GROUP BY class
    ) AS cs
WHERE
    student_count > 4;
"""

## Optimized submission from others

"""
select class
from courses
group by class
having count(student)>=5;;
"""
''' ******************************************************************************************************
NAME : Top Earners
TYPE : AGGREGATION
TOOL : COUNT()

Explanation 1 
The maximum earnings value is . 
The only employee with earnings  is Kimberly, so we print the maximum earnings value () and 
a count of the number of employees who have earned  (which is ) as two space-separated values.
'''

SELECT 
    salary * months AS earnings, COUNT(salary * months)
FROM 
    Employee
GROUP BY 
    earnings
ORDER BY 
    earnings DESC
LIMIT 1;

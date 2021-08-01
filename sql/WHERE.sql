'''
Sample Output

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2

Explanation 1

In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. 
There is one manager, M1, under senior manager SM1. 
There are two employees, E1 and E2, under manager M1.

Explanation 2
In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. 
There are two managers, M2 and M3, under senior manager SM3. 
There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.
'''

SELECT 
    c.company_code, 
    c.founder, 
    COUNT(DISTINCT l.lead_manager_code), 
    COUNT(DISTINCT s.senior_manager_code), 
    COUNT(DISTINCT m.manager_code), 
    COUNT(DISTINCT e.employee_code)
FROM 
    Company c, 
    Lead_Manager l, 
    Senior_Manager s, 
    Manager m, 
    Employee e
WHERE c.company_code = l.company_code
     AND l.company_code = s.company_code
     AND s.company_code = m.company_code
     AND m.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;

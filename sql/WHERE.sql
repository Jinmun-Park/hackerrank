''' ------------------------------------------------------------------------------------------------------------
NAME : New Companies
TYPE : Advanced Select
TOOL : WHERE(), COUNT(DISTINCT())

Sample Output

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
''' ------------------------------------------------------------------------------------------------------------
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
GROUP BY c.company_code, c.founder '''C.FOUNDER IS IMPORTANT'''
ORDER BY c.company_code;

''' ------------------------------------------------------------------------------------------------------------
NAME : The Report
TYPE : Basic Join
TOOL : WHERE(), IF()

Sample Output

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
''' ------------------------------------------------------------------------------------------------------------
SELECT 
    IF(GRADE < 8, NULL, NAME), '''Q asks for Null on Name only'''
    GRADE, 
    MARKS
FROM 
    Students S,
    Grades G
WHERE 
    S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK
ORDER BY
    G.GRADE DESC,
    NAME
    
''' ------------------------------------------------------------------------------------------------------------
NAME : Top Competitors
TYPE : Basic Join
TOOL : WHERE(), HAVING()

EXPLANATION :
Write a query to print the respective hacker_id and name of hackers who achieved full scores(*) for more than one challenge(*) 

''' ------------------------------------------------------------------------------------------------------------
SELECT 
    H.HACKER_ID,
    H.NAME
FROM
    SUBMISSIONS S INNER JOIN CHALLENGES C 
        ON S.CHALLENGE_ID = C.CHALLENGE_ID
    INNER JOIN DIFFICULTY D
        ON C.DIFFICULTY_LEVEL = D.DIFFICULTY_LEVEL
    INNER JOIN HACKERS H
        ON S.HACKER_ID = H.HACKER_ID    
WHERE
    S.SCORE = D.SCORE '''Q : HACKERS WHO ACHIEVED FULL SCORES'''
GROUP BY H.HACKER_ID, H.NAME
    HAVING COUNT(H.HACKER_ID) > 1
ORDER BY
    COUNT(H.HACKER_ID) DESC, H.HACKER_ID ASC

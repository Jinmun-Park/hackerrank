''' ------------------------------------------------------------------------------------------------------------
NAME : New Companies
TYPE : Advanced Select
TOOL : WHERE(), COUNT(DISTINCT())

Sample Output

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
------------------------------------------------------------------------------------------------------------ '''
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
------------------------------------------------------------------------------------------------------------ ''' 
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

------------------------------------------------------------------------------------------------------------ ''' 
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
    
''' ------------------------------------------------------------------------------------------------------------
NAME : Ollivanders Inventory
TYPE : Basic Join
EXPLAIN 
Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. 
Write a query to print the id, age, coins_needed, and power of the wands that Rons interested in, sorted in order of descending power. 
If more than one wand has same power, sort the result in order of descending age.
------------------------------------------------------------------------------------------------------------ ''' 

SELECT W.id, P.age, W.coins_needed, W.power ''' Q : NEEDS TO PRINT AGE,POWER AFTER GROUP BY. SO IT NEEDS TO HAVE 2 * SELECT '''
FROM WANDS AS W
    INNER JOIN WANDS_PROPERTY AS P ON W.code = P.code
WHERE P.is_evil = 0 AND (W.coins_needed, P.age, W.power) IN  
    (SELECT 
        MIN(W1.coins_needed),
        P1.age, 
        W1.power
    FROM WANDS AS W1 INNER JOIN 
        WANDS_PROPERTY AS P1 ON 
        W1.code = P1.code
    GROUP BY '''Q IS POORLY STATED. IT NEEDS TO BE GROUP BY BOTH AGE,POWER'''
        P1.age, 
        W1.power)
ORDER BY W.power DESC, P.age DESC



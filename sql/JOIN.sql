''' ******************************************************************************************************
NAME : The Report
TYPE : Basic Join

ANSWER 
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68
'''
SELECT 
    IF(GRADE < 8, NULL, NAME), 
    GRADE, 
    MARKS
FROM 
    STUDENTS JOIN GRADES
WHERE ''' JOIN WHERE'''
    MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY 
    GRADE DESC, 
    NAME

''' ******************************************************************************************************
NAME : Top Competitors
TYPE : Basic Join

ANSWER 
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68
'''
select 
    h.hacker_id, h.name
from submissions s
inner join challenges c
on s.challenge_id = c.challenge_id
inner join difficulty d
on c.difficulty_level = d.difficulty_level 
inner join hackers h
on s.hacker_id = h.hacker_id
where 
    s.score = d.score 
group by '''To count hacker_id'''
    h.hacker_id, h.name
having  '''Important'''
    count(s.hacker_id) > 1
order by 
    count(s.hacker_id) desc, s.hacker_id asc
    
''' ******************************************************************************************************
NAME : Ollivanders Inventory
TYPE : Basic Join

EXPLAIN 
Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. 
Write a query to print the id, age, coins_needed, and power of the wands that Rons interested in, sorted in order of descending power. 
If more than one wand has same power, sort the result in order of descending age.
'''
SELECT W.id, P.age, W.coins_needed, W.power
FROM WANDS AS W
    INNER JOIN WANDS_PROPERTY AS P ON W.code = P.code
WHERE P.is_evil = 0 AND W.coins_needed = '''Looking for minimun gold need '''
    (SELECT MIN(coins_needed)
     FROM WANDS AS W1
        INNER JOIN WANDS_PROPERTY AS P1 ON W1.code = P1.code
     WHERE W1.power = W.power AND P1.age = P.age) '''Question is poorly stated that it just needs combination of power&age to find the minum gold required'''
ORDER BY W.power DESC, P.age DESC

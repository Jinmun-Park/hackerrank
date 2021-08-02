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

''' ****************************************************************************************************** DIFFICULT
NAME : Challenges
TYPE : Basic Join

Write a query to print the hacker_id, name, and the total number of challenges created by each student. 
Sort your results by the total number of challenges in descending order. 
If more than one student created the *same number of challenges, then sort the result by hacker_id. 
If more than one student created the *same number of challenges and the count is less than *the maximum number of challenges created, 
then exclude those students from the result.
'''
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS challenge_counter
FROM hackers h
JOIN challenges c
    ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name

HAVING challenge_counter IN ( '''Condition 1 : unique count of channge_id'''
    SELECT aux_table.counter
    FROM(
        SELECT hacker_id, COUNT(challenge_id) AS counter 
        FROM challenges
        GROUP BY hacker_id '''Group By 1'''
    ) AS aux_table
    GROUP BY aux_table.counter '''Group By 2, reason for 2 groupby is because we have to sort by hacker_id '''
    HAVING COUNT(aux_table.counter) = 1
)
OR
challenge_counter =(
    SELECT MAX(aux_table.counter)
    FROM(
        SELECT hacker_id, COUNT(challenge_id) AS counter
        FROM challenges
        GROUP BY hacker_id
    ) AS aux_table)
ORDER BY challenge_counter DESC, h.hacker_id ASC;


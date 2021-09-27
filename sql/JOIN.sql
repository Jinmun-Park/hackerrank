''' ******************************************************************************************************
NAME : The Report
TYPE : Basic Join

EXPLAIN
Ketty doesnt want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- 
i.e. higher grades are entered first. 
If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. 
Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. 
If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

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

EXPLAIN
print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. 
Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

ANSWER 
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68
'''
SELECT 
    h.hacker_id, h.name
FROM submissions s
inner JOIN challenges c
ON s.challenge_id = c.challenge_id
inner JOIN difficulty d
ON c.difficulty_level = d.difficulty_level 
inner JOIN hackers h
ON s.hacker_id = h.hacker_id
WHERE 
    s.score = d.score 
GROUP BY '''To count hacker_id'''
    h.hacker_id, h.name
HAVING  '''Important'''
    COUNT(s.hacker_id) > 1
ORDER BY
    COUNT(s.hacker_id) DESC, s.hacker_id ASC
    
''' ******************************************************************************************************
NAME : Ollivanders Inventory
TYPE : Basic Join

EXPLAIN 
Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. 
Write a query to print the id, age, coins_needed, and power of the wands that Rons interested in, sorted in order of descending power. 
If more than one wand has same power, sort the result in order of descending age.

-- 최초 SELECT에 GROUPBY가 필요하지 않는 단순 MIN필터로 값을 찾는 문제이기에, WHERE를 이용하여 MATCHING항목만 사용.
'''
SELECT W.id, P.age, W.coins_needed, W.power
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
    GROUP BY 
        P1.age, 
        W1.power)
ORDER BY W.power DESC, P.age DESC

''' ****************************************************************************************************** DIFFICULT (READ EXPLANATION FROM QUESTION)
NAME : Challenges
TYPE : Basic Join

Write a query to print the hacker_id, name, and the total number of challenges created by each student. 
Sort your results by the total number of challenges in descending order. 
If more than one student created the *same number of challenges, then sort the result by hacker_id. 
If more than one student created the *same number of challenges and the count is less than *the maximum number of challenges created, 
then exclude those students from the result.

--- 최초 SELECT 컬럼에 GROUP BY를 활용한 COUNT(CHALLENGE_ID)가 있으므로 WHERE를 사용하기 어렵다.
--- HAVING을 이용하려면 최초 SELECT의 컬럼(CHALLENGE_ID)과 HAVING에서 사용하는 컬럼(CHALLENGE_ID)이 추가적인 GROUPBY가 필요하지 않아야한다.
--- 반면에 Contest Leaderboard의 문제는 원하는 FILTER를 매칭후에도 최초 SELECT에서 합계를 구하여 하므로, SUM(SCORE), HAVING에 적합하지 않다.
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

''' ****************************************************************************************************** 
NAME : Contest Leaderboard
TYPE : Basic Join

The total score of a hacker is the sum of their maximum scores for all of the challenges. 
Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. 
If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. 
Exclude all hackers with a total score of  from your result.

--- 최초 SELECT값에 GROUP BY를 활용하여 SUM(SCORE)를 구하여 하기에, WHERE는 적합하지 않다.
--- MAX값으로 FILTER후 최초 SELECT에서 다시한번 합계를 구하여 하므로, HAVING에 적합하지 않다.

'''
SELECT 
    h.hacker_id, 
    name, 
    sum(score) AS total_score
FROM hackers AS h inner join
    (SELECT 
        hacker_id,
        max(score) as score
     FROM 
        submissions 
     GROUP BY 
        challenge_id, 
        hacker_id) max_score
ON h.hacker_id=max_score.hacker_id
GROUP BY 
    h.hacker_id, name
HAVING 
    total_score > 0
ORDER BY 
    total_score desc, 
    h.hacker_id
''' ****************************************************************************************************** 
NAME : Placements
TYPE : Advanced Join

Write a query to output the names of those students whose best friends got offered a higher salary than them. 
Names must be ordered by the salary amount offered to the best friends. 

'''
SELECT s.Name 
FROM Students as s INNER JOIN Friends as f
    ON s.ID = f.ID
INNER JOIN Packages as p 
    ON s.ID = p.ID 
INNER JOIN 
    (SELECT Friends.Friend_ID, Packages.Salary
    FROM Friends INNER JOIN Packages 
        ON Friends.Friend_ID = Packages.ID) AS Friend_Salary
    ON f.Friend_ID = Friend_Salary.Friend_ID
WHERE Friend_Salary.Salary > p.Salary
ORDER BY Friend_Salary.Salary

''' ******************************************************************************************************
NAME : The Report
TYPE : Basic Join

--- JOIN + WHERE, JOIN을 진행할 공통 컬럼이 없을때 WHERE를 이용하여 하나의 테이블로 병합
--- 정답에는 AS로 VARIABLE을 칭하지 않았지만, AS로 칭하는것이 좋다. (아래 문제확인)
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
NAME : SQL Project Planning
TYPE : Advanced Join

--- 하나의 테이블을 두개의 테이블로 쪼개서 공통 컬럼 없이 병합하기 위해 JOIN + WHERE를 이용
--- WHERE 를 이용하지 않고 러닝을 하고 결과를 확인하면 WHERE를 쓰는 이유를 확인할수 있음.
--- MIN() 이용하여야만 START_DATE에 가장 근접한 END_DATE를 확인할수 있음.
'''
SELECT Start_Date, MIN(End_Date)
FROM 
    (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) a,
    (SELECT end_date FROM PROJECTS WHERE end_date NOT IN (SELECT start_date FROM PROJECTS)) b
where start_date < end_date
GROUP BY start_date
ORDER BY datediff(start_date, MIN(end_date)) DESC, start_date

''' ******************************************************************************************************
NAME : Symmetric Pairs
TYPE : Advanced Join

--- 하나의 테이블을 쪼개지 않고 두번 병합하여 GROUP BY + HAVING을 이용하여 컨디션에 맞춤
--- SAMPLE INPUT을 확인해야 정확한 이해가 가능.
--- ( ON f1.X=f2.Y AND f1.Y=f2.X ) + ( HAVING COUNT(f1.X)>1 ) 을 통해서 문제에서 주어진 symmetric pairs if (X1 = Y2) and (X2 = Y1)
'''
SELECT f1.X, f1.Y FROM Functions f1
INNER JOIN Functions f2 ON f1.X=f2.Y AND f1.Y=f2.X
GROUP BY f1.X, f1.Y
HAVING COUNT(f1.X)>1 or f1.X<f1.Y
ORDER BY f1.X 
    
''' ******************************************************************************************************
NAME : Top Competitors
TYPE : Basic Join

EXPLAIN
print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. 
Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.
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

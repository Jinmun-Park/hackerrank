''' ******************************************************************************************************
NAME : Type of Triangle
TYPE : Advanced Select

Explanation 1 

Equilateral: Its a triangle with  sides of equal length.
Isosceles: Its a triangle with  sides of equal length.
Scalene: Its a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C dont form a triangle.
'''

SELECT CASE             
    WHEN A + B > C AND B + C > A AND A + C > B THEN
        CASE 
            WHEN A = B AND B = C THEN 'Equilateral'
            WHEN A = B OR B = C OR A = C THEN 'Isosceles'
            ELSE 'Scalene'
        END
    ELSE 'Not A Triangle'
    END
FROM TRIANGLES;

''' ******************************************************************************************************
NAME : The PADS
TYPE : Advanced Select

SAMPLE OUTPUT

Samantha(D)
There are a total of 2 doctors.
'''

SELECT concat(name,concat('(', concat(substr(occupation,1,1),')'))) 
FROM occupations 
ORDER BY name;

SELECT concat('There are a total of',concat(' ',concat(count(occupation),concat(' ',concat(lower(occupation),'s.'))))) as total 
FROM occupations
GROUP BY occupation 
ORDER BY total;

''' ******************************************************************************************************
NAME : Binary Tree Nodes
TYPE : Advanced Select

SAMPLE OUTPUT

1 Leaf
2 Inner
3 Leaf
'''

SELECT CASE
    WHEN P IS NULL THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf')
    END
FROM BST
ORDER BY N ASC

''' ******************************************************************************************************
NAME : Occupations
TYPE : Advanced Select

SAMPLE OUTPUT


'''
SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT min(Doctor), min(Professor), min(Singer), min(Actor) '''it will return The "LOWEST" element from each column (which happened to be the first element)'''
FROM(
  SELECT case 
    when Occupation='Doctor' then (@r1:=@r1+1)
    when Occupation='Professor' then (@r2:=@r2+1)
    when Occupation='Singer' then (@r3:=@r3+1)
    when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber, '''Creating ROW NUM '''
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  FROM OCCUPATIONS
  ORDER BY Name
    ) temp
GROUP BY RowNumber;

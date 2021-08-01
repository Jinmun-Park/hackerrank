'''
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

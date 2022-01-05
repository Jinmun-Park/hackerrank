# STATEMENT
# TIPS 01


'''
summary 
001 : 
  
'''
########################################################################################################################
'''
001 : Diagonal Difference
  Topic : 
  Explain : 
'''

#Input
'''
3
11 2 4
4 5 6
10 8 -12
'''

#Output
'''
15
'''

def diagonalDifference(arr):
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-i-1]

    return abs(left - right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    #[[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

########################################################################################################################

'''
002 : Apple and Orange
  Topic : 
  Explain : 
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))


########################################################################################################################

'''
003 : Divisible Sum Pairs
  Category : Implementation
  Topic : 
  Explain : 
'''
# INPUT
'''
STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
'''
# OUTPUT
'''
 5
'''

from itertools import combinations
def divisibleSumPairs(n, k, ar):

    pairs = [sum(pair) % k for pair in combinations(ar, 2)]
    return(pairs.count(0))
########################################################################################################################

'''
004 : Migratory Birds
  Category : Implementation
  Topic : 
  Explain : 
'''
# INPUT
'''
6
1 4 4 4 5 3
'''
# OUTPUT
'''
4
'''
from collections import Counter

def migratoryBirds(arr):
    bird = Counter(arr)    
    return bird.most_common(1)[0][0]

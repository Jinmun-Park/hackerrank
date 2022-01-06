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
  
########################################################################################################################

'''
005 : Sales by Match
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
'''
# OUTPUT
'''
3
'''
from collections import Counter

def sockMerchant(n, ar):
    odd_count = 0
    c = Counter(ar)
    show = [v for i,v in c.items() if v>1]
    for i in show:
        count = i//2
        odd_count += count
    return odd_count
    bird = Counter(arr)    
    return bird.most_common(1)[0][0]
########################################################################################################################

'''
006 : Counting Valleys
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
8
UDDDUDUU
'''
# OUTPUT
'''
1
'''
# EXPLANATION
'''
_/\      _
   \    /
    \/\/
'''
def countingValleys(steps, path):
    seaLevel = valley = 0

    for step in path:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        if (step == 'U') and (seaLevel == 0): '''IMPORTANT'''
            valley += 1
            
########################################################################################################################

'''
007 : Electronics Shop
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
10 2 3
3 1
5 2 8
'''
# OUTPUT
'''
9
'''
def getMoneySpent(keyboards, drives, b):
    comb = list(itertools.product(keyboards, drives))
    comb_list = []
    for i in comb: 
        s = sum(i)
        if s <= b : 
            comb_list.append(s)
        else : 
            comb_list.append(-1)
    
    return(max(comb_list))

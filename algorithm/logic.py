'''
Algorithm
'''

'''
Tips 
'''

# TIPS 01
'''HACKERRANK FORMAT : return [] only allows you to see the result '''
def beautifulDays(i, j, k):
  return [i for i in range(i,j)]

# TIPS 02

########################################################################################################################
'''
001 : [Comming from Implementation] Apple and Orange
  Score : Complete Fail
  Reason : Logic can be built in a simpler way
  Topic : loop()
  Explain : 
'''
'''
Input
7 11
5 15
3 2
-2 2 1
5 -6
'''
'''
Output
1
1
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    print(sum([1 for num in apples if s <= (num+a) and t >= (num+a)]))
    print(sum([1 for num in oranges if s <= (num+a) and t >= (num+a)]))
    
########################################################################################################################
'''
002 : [Comming from Implementation] Number Line Jumps
  Score : -
  Reason : -
  Topic : if(), while
  Explain : 
'''

'''
Input
0 2 5 3
'''

'''
Output
NO
'''

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2 and x1 != x2: # if same speed, they will never meet
        return('NO')
    if x1 < x2 and v1 < v2:
        return('NO')
    if x1 > x2 and v1 > v2:
        return('NO')
    if x1 < x2 and v1 > v2:
        while x1 != x2: '''IMPORTANT'''
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2:
                return ('YES')
            if x1 > x2:
                return ('NO')
                break '''IMPORTANT'''
    if x1 > x2 and v1 < v2:
        while x1 != x2:
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2:
                return ('YES')
            if x1 < x2:
                return ('NO')
                break
                
########################################################################################################################
'''
003 : [Comming from Implementation] Breaking the Records
  Score : Failed
  Reason : did not know how to use loop properly
  Topic : for()
  Explain : 
'''

'''
Input
9
10 5 20 20 4 5 2 25 1
'''
'''
Output
2 4
Explanation
 Game  Score  Minimum  Maximum   Min  Max
     0      12     12        12       0   0
     1      24     12       *24       0   1
     2      10     *10       24       1   1
     3      24     10        24       1   1
'''

def breakingRecords(scores):
    # Setting your basis list
    low, high = scores[0], scores[0] '''VERY IMPORTANT'''
    highest, lowest = 0,0
    # each list can be pulled in loop from main list
    for i in scores: '''VERY IMPORTANT'''
        #10 5 20 20 4 5 2 25 1 [seqeuntly]
        if i > high:
            highest += 1
            #loop can continue in the condition
            high = i '''VERY IMPORTANT : high will be replaced if meets the condition'''
        if i < low:
            lowest += 1
            low = i
        '''Else is not needed. Then what happens to the first index ? Interesting'''
    return (highest, lowest)
########################################################################################################################
'''
004 : [Comming from Implementation] Subarray Division
  Score : Failed
  Reason : did not know how to use loop properly
  Topic : for()
  Explain : 
'''

'''
Input
5
1 2 1 3 2
3 2
'''

'''
Output
2
'''

def birthday(s, d, m):
    # s = 1 2 1 3 2
    # d = 3 
    # m = 2
    # 'm' is to be dived into two elements that should be equal to 'd'
    count = 0    
    for i in range(0,len(s)+1-m): #range(0, 5+1-2 = 4)
        if sum(s[i:i+m]) == d: '''IMPORTANT : enable to sum in the range. The range of sum will also move'''
        #s[0:2],,s[1:3],, == 3 
            count+=1
    return count
  
########################################################################################################################
'''
005 : [Comming from Implementation] Migratory Birds
  Score : Failed
  Reason : Forgot most_common()
  Topic : Counter()
  Explain : 
'''

'''
Input
6
1 4 4 4 5 3
'''

'''
Output
4
'''

from collections import Counter

def migratoryBirds(arr):
    #a = sorted(counter.most_common(1)[0], reverse = True)[0] Fail i dont know why
    return(Counter(sorted(arr)).most_common(1)[0][0])
  
########################################################################################################################
'''
005 : [Comming from Implementation] Sales by Match
  Score : Success
  Reason : -
  Topic : Counter()
  Explain : 
'''

'''
Input
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
'''

'''
Output
3
(Only matching sox can be use, 2 or 3)
'''

def sockMerchant(n, ar):
    count = Counter(ar)
    c = 0
    for i,v in count.items(): # v is number of count
        if v % 2 == 0:
            c+=(v/2)
        elif (v % 2 != 0) and (v > 1):
            c+=((v-1)/2)
    return int(c)
    #return ([i for i,v in count.items() if v % 2==0])
########################################################################################################################
'''
006 : [Comming from Implementation] Drawing Book
  Score : Failed
  Reason : -
  Topic : Min()
  Explain : Problem in understanding logic
'''
'''
Input
6 (Total number of Page)
2 (Page wants to search)
'''
'''
Output
3
'''

def pageCount(n, p):
    return(min(p//2, n//2 - p//2))
    #return min(p//2, (n-p)//2) Does not work
########################################################################################################################
'''
007 : [Comming from Implementation] Counting Valleys
  Score : Failed
  Reason : -
  Topic : -
  Explain : Problem in understanding logic
'''
'''
Input
8
UDDDUDUU
'''
'''
Output
1
Understanding
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
        if (step == 'U') and (seaLevel == 0):
            valley += 1
########################################################################################################################
'''
008 : [Comming from Implementation] Electronics Shop
  Score : Success
  Reason : -
  Topic : -
  Explain : -
'''
'''
Input
10 2 3
3 1
5 2 8
'''
'''
Output
9
'''
import itertools

def getMoneySpent(keyboards, drives, b):
    comb = list(itertools.product(keyboards, drives)) '''IMPORTANT'''
    # Two lists can have a combination using 'product'
    comb_list = []
    for i in comb: 
        s = sum(i)
        if s <= b : 
            comb_list.append(s)
        else : 
            comb_list.append(-1)
    
    return(max(comb_list))
########################################################################################################################
'''
009 : [Comming from Implementation] Cats and a Mouse
  Score : Half
  Reason : Single line return
  Topic : -
  Explain : -
'''
def catAndMouse(x, y, z):
    a = abs(z-x)
    b = abs(z-y)
    return "Cat A" if a<b else "Cat B" if b<a else "Mouse C"
########################################################################################################################
'''
010 : [Comming from Implementation] Climbing the Leaderboard
  Score : Failed
  Reason : index can be measured using len(), but enumerate() is complex.
  Topic : len(), for() + while
  Explain : ****Cannot understand logic yet
'''
'''
INPUT
100 90 90 80 75 60
50 65 77 90 10
'''
def climbingLeaderboard(ranked, player):
    scores_set = list(set(ranked))
    scores_set.sort(reverse=True)
    # 100 90 90 80 75 60
    # 100 90 80 75 60
    result = []
    l = len(scores_set) #5 
    
    for s in player: 
      # player = 50 65 77 90 10
        '''IMPORTANT : [l-1] is the last element in the list'''
        #s1 = l = 5
        while (l>0) and (s >= scores_set[l-1]): # l = 5, l = 5, l = 4, l = 3
            l -= 1 # 
        result.append(l+1) 

    return result
########################################################################################################################
'''
011 : [Comming from Implementation] Diagonal Difference

'''
'''
11
   5
     -12
     4
   5
10
'''
def diagonalDifference(arr):
    primSum = 0
    secSum = 0    
    
    for row in range(n): #n = 3
        primSum += arr[row][row] #arr[0][0],,,[2][2]
        secSum += arr[row][n - 1 - row] #arr[0][2],,,
    return abs(primSum - secSum)

########################################################################################################################
'''
012 : [Comming from Implementation] Designer PDF Viewer
'''
'''
INPUT
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
OUTPUT
9
'''
from itertools import product

def designerPdfViewer(h, word):
    l =[]
    for i in word:
        l.append(h[ord(i)-ord('a')]) '''ord(i) givs the sequence of word in ACSI. If we deduct from the first word 'a'.'''
    return (len(l)*max(l))

########################################################################################################################
'''
013 : [Comming from Implementation] Compare the Triplets
'''
'''
INPUT
5 6 7
3 6 10

OUTPUT
1 1

Explanation
A : (5>3) point 1, 
B : (10>7) point 1
1 1
'''
def compareTriplets(a, b):
    score = [0, 0] '''IMPORTANT : This is the only way to present answer accordingly'''
    for a, b in zip(a, b): '''HACKER FORMAT : a[] b[] format will not show us the value'''
        if a > b:
            score[0]+= 1
        elif b > a:
            score[1]+=1
    return score
    
########################################################################################################################
'''
014 : [Comming from Implementation] Angry Professor
'''
'''
INPUT
2
4 3  *(n=4, k=3)
-1 -3 4 2
4 2
0 -1 2 1

OUTPUT
YES
NO

Explanation
if a[i] > 0 is late, a[i] =< 0 is early
'''
def angryProfessor(k, a):
    early = 0 
    late = 0
    for i in a:
        if int(i) > 0:
            late = late + 1
        elif int(i) <= 0:
            early = early + 1

    return("NO" if k <= early else "YES")  '''way format is matter in return'''
    
########################################################################################################################
'''
015 : [Comming from Implementation] Beautiful Days at the Movies
'''
'''
INPUT
20 23 6

OUTPUT
2

Explanation
1. range(20,23+1)
2. make reversed : int(str(day)[::-1]. for example 20 -> 2 / 21 -> 12
3. then |20-21|/k. if its divisibe then count 1
'''
def beautifulDays(i, j, k):

    beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
    return(sum(beautifulDays))
    ''' HACKERRANK FORMAT : return [i for i in range(i,j)] '''
    
########################################################################################################################
https://www.hackerrank.com/challenges/the-hurdle-race/problem

'''
Algorithm
'''

'''
Tips 
'''

# TIPS 01


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
            high = i '''VERY IMPORTANT'''
        if i < low:
            lowest += 1
            low = i
    return (highest, lowest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
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
        if sum(s[i:i+m]) == d: #s[0:2],,s[1:3],, == 3
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
'''

def sockMerchant(n, ar):
    count = Counter(ar)
    c = 0
    for i,v in count.items():
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
  Explain : Cannot understand logic yet
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

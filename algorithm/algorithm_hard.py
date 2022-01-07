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
    return(pairs.count(0)) '''divisible is 0'''
  
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
        s = sum(i) ''' sum the combination '''
        if s <= b : 
            comb_list.append(s)
        else : 
            comb_list.append(-1)
    
    return(max(comb_list))
########################################################################################################################

'''
008 : Angry Professor
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
2
4 3
-1 -3 4 2 (--> a)
4 2
0 -1 2 1 (--> a)
'''
# OUTPUT
'''
YES
NO
'''
def angryProfessor(k, a):
    
    l = list()
    n = len(a)
    
    for i in range(n):
        if a[i] < 1:
            l.append(i)
    
    if len(l) < k:
        return 'YES' '''return text'''
    else:
        return 'NO'
########################################################################################################################

'''
009 : Beautiful Days at the Movies
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
20 23 6
'''
# OUTPUT
'''
2
'''
def beautifulDays(i, j, k):
    daycount = int(0)
    for x in range(i, j+1):
        if (x - int(str(x)[::-1])) % k == 0: '''[::-1] means opposite, but int(str(x)[::-1]) is the most important'''
            daycount += 1
    return daycount
########################################################################################################################

'''
010 : Save the Prisoner!
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
2
5 2 1
5 2 2
'''
# OUTPUT
'''
2
3
'''

'''
n = 4 -> 1,2,3,4 
m = 6 -> 2,3,4,1,2,3 (answer is 3)
s = 2 -> start point 2
'''
def saveThePrisoner(n, m, s):
    if((m + s -1)%n == 0):
        return(n)
    else:
        return ((m+s-1)%n) '''IMPORTANT : remainder is very useful to count again (for ex. 1,2,3)'''

'''
print(2%8) = 2
print(7%4) = 3
'''
########################################################################################################################

'''
011 : Circular Array Rotation
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
3 2 3
1 2 3
0
1
2
'''
# OUTPUT
'''
2
3
1
'''

'''
n = 3, k = 2, q = 3
n = [1,2,3]
change the digit k = 2
[3,1,2] -> [2,3,1] 
The right format to get this is "len(a) -k"
"a[k:] + a[:k]"
'''
def circularArrayRotation(a, k, queries):
    if k > len(a):
        k = k % len(a)
    k = len(a) - k '''IMPORTANT'''
    a = a[k:] + a[:k] '''IMPORTANT'''
    return [a[i] for i in queries]
########################################################################################################################

'''
012 : Sequence Equation
  Category : 그냥 외워
  Topic : 
  Explain : 
'''
# INPUT

def permutationEquation(p):
    for i in range(1,len(p)+1):
        return p.index(p.index(i)+1)+1
        
########################################################################################################################

'''
013 : Jumping on the Clouds: Revisited
  Category : 처음에 정답이 이해가 안갔고, 나중에 했는데도 어떻게 이 답이 나왔는지 
  Topic : 
  Explain : 
'''
# INPUT
'''
STDIN             Function
-----             --------
8 2               n = 8, k = 2
0 0 1 0 0 1 1 0   c = [0, 0, 1, 0, 0, 1, 1, 0]
'''
# OUTPUT
'''
92
'''
def jumpingOnClouds(c, k):
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    
    return energy
        
########################################################################################################################

'''
014 : Find Digits
  Category : 
  Topic : 
  Explain : 
'''
# INPUT
'''
2
12
1012
'''
# OUTPUT
'''
2
3
'''
def findDigits(n):
    number = list(str(n)) '''input is "1012." list(str()) is important -> ['1','2,','3','4']'''
    count = 0
    for i in range(len(number)):
        try:
            if n % int(number[i]) == 0: '''sequence'''
                count+=1
        except ZeroDivisionError:
            pass
    return count
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
########################################################################################################################

'''
015 : Sherlock and Squares
  Category : 루트 값을 찾아 (그냥외워)
  Topic : 
  Explain : 
'''

def squares(a, b):
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    
    return (sqrtB - sqrtA + 1)
########################################################################################################################

'''
016 : Library Fine
  Category : 
  Topic : 
  Explain : 
'''

def libraryFine(d1, m1, y1, d2, m2, y2):
    day = d2 - d1
    month = m2 - m1
    year = y2 - y1
    
    if year < 0:
        fine = 10000
    elif (year == 0) and (month < 0):
        fine = abs(month) * 500
    elif (year == 0) and (month == 0) and (day < 0): '''FORGOT TO PUT (day < 0) '''
        fine = abs(day) * 15
    else:
        fine = 0
    
    return fine
  
########################################################################################################################

'''
016 : Cut the sticks


  Category : 
  Topic : 
  Explain : 
'''

def cutTheSticks(arr):
    l = list()
    l.append(len(arr))
    while True: '''WHILE 을 쓰질 못함'''                 
        arr = [x for x in arr if x != min(arr)] 
        if len(arr)==0:
            break '''break point'''
        l.append(len(arr))
    return l
########################################################################################################################

'''
017 : Repeated String
  Category : 
  Topic : 
  Explain : 
'''
#INPUT
'''
aba
10
'''
#OUTPUT
'''
7
'''
'''
string a 를 세는것이 문재
aba -> 10digits -> aba aba aba a -> 마지막 a를 세기위해서는 s[:n % len(s)].count("a") -> s[:1] 이부분이 
'''

def repeatedString(s, n):
    y = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    return y
        

########################################################################################################################
'''
001 : [Comming from Implementation] Organizing Containers of Balls
  Score : Failed
'''
'''
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
'''
def organizingContainers(container):
    # Write your code here
    r = sorted([sum(x) for x in container])
    c = sorted([sum(x) for x in zip(*container)])
    return "Possible" if r == c else "Impossible"
########################################################################################################################
'''
002 : [Comming from Implementation] Encryption
  Score : Failed
'''
'''
INPUT
haveaniceday

OUTPUT
hae and via ecy

EXPLANATION
have
anic
eday

loop(len(character)) then ceiling and floor
'''
def encryption(s):
    s.replace(" ", "")
    a = math.ceil(math.sqrt(len(s)))
    return " ".join([s[i::a] for i in range(a)]) '''[i::a] : Transpose. This works as *transpose(range(a,b,c))'''
########################################################################################################################
'''
003 : [Comming from Implementation] Absolute Permutation
  Score : Failed
  Topic : Permutation()
'''
'''
INPUT
STDIN   Function
-----   --------
3       t = 3 (number of queries)
2 1     n = 2, k = 1
3 0     n = 3, k = 0
3 2     n = 3, k = 2

OUTPUT
2 1
1 2 3
-1

EXPLANATION
pos[i]  i   |pos[i] - i|
  3     1        2
  4     2        2
  1     3        2
  2     4        2
'''
def absolutePermutation(n, k):
    res = list()
    for i in range(1,n+1):'''IMPORTANT : Condition 1'''
        if 1<=i+k<=n:
            res.append(i+k)
        if k!=0 and i%k==0: '''IMPORTANT : Condition 2. when this condition meets when pos[i] = 0. Example) n = [2] k = [2]'''
            k=(-1)*k '''IMPORTANT : pos[i] = 0 element will not show in the list. This will be filtered out **len(res)!=n'''
    if len(res)!=n:'''IMPORTANT : The way to put n constraints on your pos[i] where pos[i] should be in the range of n'''
        return [-1]
    return res 
########################################################################################################################

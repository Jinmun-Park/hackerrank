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
    # Write your code here
    
    apple_count = 0
    orange_count = 0
    
    print(sum([1 for num in apples if s <= (num+a) and t >= (num+a)]))
    print(sum([1 for num in oranges if s <= (num+a) and t >= (num+a)]))
    
########################################################################################################################

'''
002 : [Comming from Implementation] Number Line Jumps
  Score : -
  Reason : -
  Topic : -
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
        while x1 != x2:
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2:
                return ('YES')
            if x1 > x2:
                return ('NO')
                break
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

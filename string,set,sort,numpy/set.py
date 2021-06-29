'''
Set
'''
'''
Tips 
'''
# STATEMENT


# TIPS 01


'''
summary 
001 : 
  
'''
########################################################################################################################
'''
001 : No Idea!
  Score : Fail
  Reason : Did not know how to create loop function properly / Intersection does not work due to question constraints
  Topic : set(),for()
  Explain : Count sub-elements match with element 
'''
#Input
'''
3 2
1 5 3
3 1
5 7
'''
#Output
'''
1
'''
n,m = input().split()
array = input().split()
#We do not use set() due to the constraints set in questions
#print(array) : ['1', '5', '3']
A = list(set(input().split())) 
#print(A) : ['1', '3']
B = list(set(input().split()))

count = 0
for i in array:
# 1,5,3
    if i in A:
    # if each 1,5,3 is in 1, 3
        count+=1
    elif i in B:
        count-=1
print(count)

########################################################################################################################
'''
002 : Symmetric Difference
  Score : Success (But enormous googing for this simple question)
  Reason : convert set -> list took long time
  Topic : set()
  Explain : Count sub-elements match with element 
'''
#Input
'''
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
'''
#Output
'''
5
9
11
12
'''
m = int(input())
a = set(input().split())
n = int(input())
b = set(input().split())

col_a = list(a.difference(b)) #list
col_b = list(b.difference(a)) #list
collect = (*col_a, *col_b) # ('5', '9', '12', '11')
collect = sorted([int(i) for i in collect]) #[] is important

print(*collect,sep='\n')


########################################################################################################################

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
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
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

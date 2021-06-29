'''
Summary of sorted() 
'''

'''
Tips 
'''
# TIPS 01
any([1>0,1==0,1<0]) '''True'''
all(['a'<'b','b'<'c']) '''True'''

# TIPS 02
all([int(i)>0 for i in n])
any([j == j[::-1] for j in n]))

########################################################################################################################

'''

001: [Coming from String]Merge the Tools!
  Score : Failed
  Reason : Tried using Counter() instead of Set(). This happened because i did not know how to use sorted(key)
  Topic : sorted(set(), key =)
  Explain : Find the unique character and print
'''
#Input
'''
s = 'AABCAAADA'
k = 3
'''
#Output
'''
AB
CA
AD
'''
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        sort = sorted(set(string[i:i+k]), key = string[i:i+k].index)
        print(''.join(sort))
########################################################################################################################
'''
002: [Coming from Set]The Captain's Room
  Score : Success
  Reason : 
  Topic : Counter() and for()
  Explain : from collections import Count / unique characted
'''
#Input
'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 **8 4 3 1 5 6 2 
'''
#Output
'''
8
'''
from collections import Counter
k = int(input())
room = list(map(int, input().split()))

cap_room = Counter(room)
print(*[i for i,v in cap_room.items() if int(v) == 1]) # I do not know *[] only shows the result lol
########################################################################################################################
'''
003 : [Comming from Built-Ins] Any or All
  Score : Fail
  Reason : First time using
  Topic : any() / all()
  Explain : any() and all() returns True or False
'''
#Input
'''
5
12 9 61 5 14 

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer. (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22,,,)
'''
#Output
'''
True
'''
N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))
########################################################################################################################
'''
004 : [Comming from Built-Ins] ginortS
  Score : -
  Reason : -
  Topic : -
  Explain : -
'''
#Input
'''
Sorting1234
'''
#Output
'''
ginortS1324
'''
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

# https://www.hackerrank.com/

'''
Introduction (Easy ~ Medium)
Print Function

Sample Input 0
3
Sample Output 0
123

'''

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    
    for i in range(n):
        print(i+1,end="")

#############################################################################################################
        
'''
Basic Data Type (Easy ~ Medium)
Find the Runner-Up Score!

Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
Explanation 0

Given list is 2 3 6 6 5. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

if __name__ == '__main__':
    n = int(raw_input()) #n = 5
    arr = map(int, raw_input().split()) #[2, 3, 6, 6, 5] convert all the strings to integers.
    arr = list(set(list(arr))) #[2, 3, 6, 5] # unorderd, unique
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])
    
#############################################################################################################

'''
Basic Data Type (Easy ~ Medium)
Nested Lists

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

Explanation 0
the lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    score_list = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        score_list.append([name, score])    
        
    second_highest = sorted(set([score for name, score in score_list]))[1]
    print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
    
#############################################################################################################
'''
Basic Data Type
List

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
if __name__ == '__main__':
    N = int(raw_input())
    the_list = list()

    for _ in range(N):
        query = raw_input().split()
        if query[0] == "print":
            print(the_list)
        elif query[0] == "insert":
            the_list.insert(int(query[1]), int(query[2]))
        elif query[0] == "remove":
            the_list.remove(int(query[1]))
        elif query[0] == "append":
            the_list.append(int(query[1]))
        elif query[0] == "sort":
            the_list = sorted(the_list)
        elif query[0] == "pop":
            the_list.pop()
        elif query[0] == "reverse":
            the_list.reverse()

#############################################################################################################
'''
String
Merge the Tools!

Sample Input 0
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output 0
AB
CA
AD
'''
from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0, len(string), k): #0,3,6
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))
#############################################################################################################   
'''
Collections
Collections.OrderedDict()

Sample Input 0
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output 0
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
from collections import*;
N = int(input());
d = OrderedDict();

for i in range(N):
    item = input().split()
    itemPrice = int(item[-1]) # last array [12, 30, 10,,,]
    itemName = " ".join(item[:-1]) # Everything excel last array
    if(d.get(itemName)): # Filter the same, filter out
        d[itemName] += itemPrice
    else:
        d[itemName] = itemPrice
        
for i in d.keys():
    print(i, d[i])
#############################################################################################################
'''
Sets
Symmetric Difference

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output

5
9
11
12
'''

numbers1 = int(raw_input()) # Important to call inputs into raw_input()
set1 = set(map(int,raw_input().split())) # split the text then map with int, lastly put into set for difference()
numbers2 = int(raw_input())
set2 = set(map(int,raw_input().split()))
set3 = (set1.difference(set2)).union(set2.difference(set1))
for i in sorted(list(set3)):
        print i
        
#############################################################################################################

'''
Sets
No idea

Sample Input
1 5 3
3 1
5 7

Sample Output
1
'''
space = set(map(int,raw_input().split()))
n = map(int,raw_input().split()) 
# Excluding Set is important, making list later in loop deducts your mark
A = set(map(int,raw_input().split()))
B = set(map(int,raw_input().split()))
#union = A.union(B)
#happiness = A.intersection(n)
#sadness = B.intersection(n)
#total = len(happiness)-len(sadness)
#print(total)

counter = 0
for i in n:
    if i in A:
        counter += 1
    elif i in B:
        counter -= 1

print counter

#############################################################################################################

'''
Sets
sets.add

Sample Input
7
UK
China
USA
France
New Zealand
UK
France 

Sample Output
5
'''

N = int(raw_input())
countries = set()

for i in range(N):
    countries.add(raw_input()) # It does not need to put raw_input() manually. Use looping to list down

print(len(countries))

#############################################################################################################
'''
Sets
Set .discard(), .remove() & .pop()

Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output
4
'''
n = int(input())
s = set(map(int, input().split())) # element for remove/discard/pop. Hence, this has to be set
num = int(input()) #Number of commands

for i in range(num):
    ip = input().split() #query
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))
#############################################################################################################   
 '''   
Sets
Set Mutations16

Sample Input
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
# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input()) # This sometimes needs to be int(), not need int()
set1 = set(map(int, input().split()))
n2 = int(input())

for i in range(n2):
    query = input().split()
    if query[0] == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        set1.intersection_update(temp_storage)
    elif query[0] == 'update':
        temp_storage = set(map(int, input().split()))
        set1.update(temp_storage)
    elif query[0] == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        set1.symmetric_difference_update(temp_storage)
    elif query[0] == 'difference_update':
        temp_storage = set(map(int, input().split()))
        set1.difference_update(temp_storage)
    else :
        assert False
    
print(sum(set1))        
#############################################################################################################
'''   
Sets
Set Mutations16

Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

Sample Output
8
'''
N = int(input())

storage = map(int, input().split())
storage = sorted(storage)

for i in range(len(storage)):
    if(i != len(storage)-1):
        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):
            print(storage[i])
            break;
    else:
        print(storage[i])
#############################################################################################################
'''   
Sets
Check Strict Superset

Sample Input
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78 
2
1 2 3 4 5
100 11 12

Sample Output
False
'''
storage = set(input().split())
N = int(input())
output = True

for i in range(N):
    storage2 = set(input().split()) # By setting this, 2 input can be stored inside this loop
    if not storage2.issubset(storage):
        output = False

print(output)
#############################################################################################################
'''   
Math
Integers Come In All Sizes
Sample Input
9
29
7
27

Sample Output
4710194409608608369201743232  
'''
print(a**b+c**d)
#############################################################################################################
'''   
Itertools
Integers Come In All Sizes

Sample Input
 1 2
 3 4
AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

Sample Output
 (1, 3) (1, 4) (2, 3) (2, 4)  
'''
from itertools import product
a=list(map(int, input().split())) # Now we have list(), not set()
b=list(map(int, input().split()))

output = product(a,b)

for i in output:
    print(i, end = " ");
#############################################################################################################
'''   
Itertools
Integers Come In All Sizes

Sample Input
HACK 2

Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH  

Sample Output
A
C
H
K
AC
AH
AK
CH
CK
HK

Sample Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
from itertools import permutations
S = list(input().split())

for i in sorted(permutations(S[0], int(S[1]))): #permutations has different way to laydown datasets
    print(''.join(i)) 
#############################################################################################################
from itertools import combinations

input = input().split()
S = input[0]
k = int(input[1])

for i in range(1,k+1): #combinations has different way to laydown datasets
    for j in combinations(sorted(S),i): # all possible combinations (= at least)
        print("".join(j))
        
from itertools import combinations_with_replacement
lis = input().split(' ')
#############################################################################################################
for i in combinations_with_replacement(sorted(lis[0]), int(lis[1])):
    print(''.join(i))
#############################################################################################################

'''   
Itertools
Integers Come In All Sizes

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
'''
from itertools import *

io = input()

for i,j in groupby(map(int,list(io))):
    print(tuple([len(list(j)), i]) ,end = " ") # This is tuple
#############################################################################################################
'''
Collection
collections.Counter()

Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200
'''

from collections import Counter
X = int(input())
key = Counter(map(int,input().split()))
N = int(input())

earnings = 0
for customer in range(N): #{5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1}
    size, x_i = map(int,input().split()) # bring the list (6,55) -> size=6, x_i=55
    if size in key and key[size] > 0: 
        key[size] -= 1 # size limitation with the count 
        earnings += x_i
            
print(earnings)

#############################################################################################################
'''
Collection
collections.namedtuple()

Sample Input
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

Sample Output
78.00
'''
from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0

for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split() #bring the list
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))

#############################################################################################################

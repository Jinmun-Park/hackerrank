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
# Sort using Set
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
# Sort using sort(set)
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
        name = raw_input() #given default, [Harry], [Berry]
        score = float(raw_input()) #37.21,,,
        score_list.append([name, score])    
        
    second_highest = sorted(set([score for name, score in score_list]))[1]
    print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
    
#############################################################################################################
# Sort using list
'''
Built-Ins
Athlete Sort

Sample Input 0
5 3 #m/n
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1 #k

Sample Output 0
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input()) #k=1
    arr.sort(key = lambda x : x[k]) # sort is important after append
    for i in arr:
        print(*i)   
#############################################################################################################
# sort in condition
'''
Built-Ins
ginortS

Sample Input 0
Sorting1234

Sample Output 0
ginortS1324

#
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')
# isdigit - last / islower - first
#############################################################################################################
# if else (list)
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
# if else (deque)
'''
Collection
Collections.deque()

Sample Input 0
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output 0
1 2

'''
from collections import deque

N = int(input())
d = deque()

for i in range(N):
    input_list = list(input().split()) ### This has to be extremely carefull
    
    if input_list[0]=='append':
        d.append(int(input_list[1]))
    elif input_list[0]=='appendleft':
        d.appendleft(int(input_list[1]))
    elif input_list[0]=='popleft':
        d.popleft()
    elif input_list[0]=='pop':
        d.pop()
        
for i in d: #This is needed almost everytime
    print(i,end=" ")

#############################################################################################################
# if not (text)
'''
Python Functionals
Validating Email Addresses With a Filter

Sample Input 0
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output 0
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

'''
def fun(s):
    try:
        user, www = s.split("@") #qqq@gmail.com
        web, ext = www.split(".") #gmail com
        if not user or not web or not ext:     # if user/web/ext is any kind of zero or empty container
            return False
        return not any([user != "".join(filter(lambda x: x.isalnum() or x in ["_", "-"], user)),
            web != "".join(filter(lambda x: x.isalnum(), web)) , len(ext)>3])
    except:
        return False
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

#############################################################################################################
# orderdictionary (fromkeys)
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
from collections import OrderedDict # Orderdictionary shows unique

def merge_the_tools(string, k):
    for i in range(0, len(string), k): #0,3,6
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))
        
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
#############################################################################################################   
# orderdictionry (sum)
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
    itemName = " ".join(item[:-1]) # Everything excep last array / [BANANA]
    if(d.get(itemName)): # Filter the same, filter out / # itemName in d
        d[itemName] += itemPrice
    else:
        d[itemName] = itemPrice
        
for i in d.keys():
    print(i, d[i])
#############################################################################################################
# orderdictionary (wordorder)
'''
Collections
Word Order

Sample Input 0

4
bcdef
abcdefg
bcde
bcdef

Sample Output 0

3
2 1 1

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. 
The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
'''
import collections;

N = int(input())
d = collections.OrderedDict() ###### This is important

for i in range(N):
    word = input()
    if word in d: #if(d.get(word)) should be same
        d[word] +=1
    else:
        d[word] = 1

print(len(d));

for k,v in d.items():
    print(v,end = " ");

#############################################################################################################
# Counter (in condition, count=0)
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

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.
'''

from collections import Counter
X = int(input())
key = Counter(map(int,input().split())) #{5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1}
N = int(input())

earnings = 0
for customer in range(N): 
    size, x_i = map(int,input().split()) # bring the list (6,55) -> size=6, x_i=55
    if size in key and key[size] > 0: #key[size], {5:2,,,,} then choose 2 and we are sequently deleting it in key[size]=-1
        key[size] -= 1 # size limitation with the count 
        earnings += x_i
            
print(earnings)

#############################################################################################################
# Counter (sorted, in condition)
'''
Collection
Company Logo

Sample Input
aabbbccde

Sample Output
b 3
a 2
c 2
'''
# Default
import math
import os
import random
import re
import sys

# Library
import collections

if __name__ == '__main__':
    s = sorted(input().strip())
    s_counter = collections.Counter(s).most_common()
    s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
    #Sort in descending order of occurrence count/ characters in alphabetical order.
    for i in range(0, 3):
        print(s_counter[i][0], s_counter[i][1])
#############################################################################################################
# Set(Union)
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
# Set (count = 0)
'''
Sets
No idea

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1

Explanation
Happiness (3-1) - (5-no array) = 1
'''
io = input().split()
m = int(io[0]) #3
n = int(io[1]) #2

storage = list()
count = 0 # count 0~

storage = list(map(int, input().strip().split())) #1,5,3

A = set(map(int, input().strip().split())) #3,1
B = set(map(int, input().strip().split())) #5,7

for i in storage: # 1,5,3
    if i in A:
        count = count+1
    if i in B:
        count = count-1

print(count)

#############################################################################################################
# Set (add)
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
# set (discard, remove, pop)
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
# set (mutation)
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
# Set (complex sort)
'''   
Sets
The Captain's Room

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
############################################################################################################# IMPORTANT (input method)
# Set (if not)
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
# math
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
# math (eval)
'''   
Built-Ins
input()
Sample Input
1 4
x**3 + x**2 + x + 1

Sample Output
True  
'''
x, k = map(int, input().split()) # layout 1 as x is very important
string = input().strip()

if eval(string) == k: #eval allows to solve the math which it has already saved
    print(True)
else:
    print(False)
#############################################################################################################
# math (list)
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
# tuple (sort)
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
# tuple (sort, count = 0)
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
    MARKS, CLASS, NAME, ID = input().split() #bring the list (all the list has already saved under the column, so we can bring the column name)
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))
#############################################################################################################
'''
Date and Time
Calendar Module

Sample Input
08 05 2015

Sample Output
WEDNESDAY
'''
import calendar

m, d, y = map(int, input().strip().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())
#############################################################################################################
'''
Errors and Exception
Exceptions

Sample Input
3
1 0
2 $
3 1

Sample Output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''
x = int(input());
for i in range(x):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e);
    except ValueError as v:
        print("Error Code:",v);
############################################################################################################# IMPORTANT
'''
Python Functionals
Reduce Function

Sample Input
3
1 2
3 4
10 6

Sample Output
5 8

(1/2)*(3/4)*(10/6) = (5/8))
'''
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda x, y: x * y, fracs)) #fracs is already defined in __name__
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split()))) ## This is important, this makes (1/2) and (3/5) 
    result = product(fracs)
    print(*result)
    
############################################################################################################# 

'''
Built-Ins
Zipped!

>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]

Sample Input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output
90.0 
91.0 
82.0 
90.0 
85.5  

Explain
Marks obtained by student 1: (80 + 90 + 91) /3
'''
n, m = map(int,input().split())
score = list() # [] also fine

for i in range(m):
    items = map(float, input().split())
    score.append(items)

# print(zip(*score)) will not show anything. it has to be in loop
 
for i in zip(*score):  # *score removes the list in zip function
    print(sum(i)/len(i)) 
#############################################################################################################
'''
Built-Ins
Any or All

######## palindromic integer ########

Sample Input
5
12 9 61 5 14 

Sample Output
True
'''
def isPositive(i):
    if i > 0:
        return True
    return False

def isPalindrome(i):
    if int(str(i)[::-1]) is i:
        return True
    return False

N = int(input())
storage = list(map(int, input().split()))
storage = sorted(storage)

if all([isPositive(i) for i in storage]):
    if any([isPalindrome(i) for i in storage]):
        print("True")
    else:
        print("False")
else:
    print("False")
#############################################################################################################

#############################################################################################################
############################################### VERY HARD ###################################################
#############################################################################################################

'''
Collection 
Pilling Up!

Sample Input
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

Sample Output

Yes
No
'''
from collections import deque

N = int(input())

for _ in range(N):
    flag = True
    input()   # This allows to select 'd' to blocks inputs deque[4,3,2,1,3,4], deque[1,3,2]
    d = deque(map(int, input().strip().split()))
    if(d[0] >= d[-1]): #[4,4] [1,2] 
        max = d.popleft() #[4] 
    else:
        max = d.pop() #[]
    while d:
        if(len(d)==1):
            if(d[0] <= max):
                break
            else:
                flag = False
                break
        else:
            if(d[0]<=max and d[-1]<=max): #[4]>=[4], [4]<=[4]
                if(d[0]>=d[-1]):
                    max = d.popleft()
                else:
                    max = d.pop()
            elif(d[0]<=max):
                max = d.popleft()
            elif(d[-1]<=max):
                max = d.pop()
            else:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
        
#############################################################################################################
############################################### VERY HARD ###################################################
#############################################################################################################

'''
Collection 
DefaultDict Tutorial

Sample Input
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output

1 2 4
3 5
'''
from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split()) #5, 2

for i in range(n):
    d[input()].append(str(i + 1))
   
for j in range(m):
    print(' '.join(d[input()]) or -1)

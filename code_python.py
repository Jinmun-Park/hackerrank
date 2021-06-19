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
    

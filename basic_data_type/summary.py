'''
basci_data_types
'''
'''
TIPS
'''
#TIP 01
for count, value in enumerate(values, start=1):
    print(count, value)
#1 a
#2 b
#3 c

#TIP 02
my_set = set("HelloWorld")
print(my_set)
#{'H', 'l', 'r', 'W', 'o', 'd', 'e'}

#TIP 03 
string = AABCAAADA
k = 3

for i in range(0,len(string),k):
    sort = sorted(set(string[i:i+k]), key = string[i:i+k].index)
    print(''.join(sort))
#AB
#CA
#AD

#TIP 04 
s = set(map(int, input().split())) 
# With map {1,2,3} 
# without map {'1','2','3'}
'''
summary 
001 : set() 
  - Every set element is unique (no duplicates) and must be immutable (cannot be changed) and unordered.
  - It helps to put unique values in 'dictionary' format
  - This helps to sort unique array
  
002 : enumerate()
  - Gives 'Count' and 'Value' in the 'list'
  - [v for i, v in enumerate(iterable, start=1) if not i % 2]
  - myList = [1, 2, 3, 100, 5]
  - [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])] *x:x[1]는 Value값을 기준으로 sort
'''
########################################################################################################################

'''
001 : Nested List
  Score : Failed 
  Reason : Tried to solve using enumerate()
  Topic : set() 
  Explain : Choose the second highest score and filter using list
'''
#Input
'''
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
'''
#Output
'''
Berry
Harry
'''

#Correct
if __name__ == '__main__':
  ls = []
  for _ in range(int(input())):
    name = input()
    score = float(input())
    ls.append([name,score])
#[['Harry', 37.21], ['Berry', 37.21],,,]] : This is nested list
second_highest = sorted(set(score for name, score in ls))[1]  '''IMPORTANT'''
#print(set([score for name, score in ls])) : {41.0, 37.2, 37.21, 39.0}
print('\n'.join(sorted([name for name, score in ls if score == second_highest])))

#Wrong
def even_items(iterable):
  return [v for i, v in enumerate(iterable, start=1) if not i % 2]

myList = [1, 2, 3, 100, 5]
[i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]

########################################################################################################################

'''
002 : Find runner-up score
  Score : Success 
  Reason : -
  Topic : set() 
  Explain : Choose the second largest and filter using list
'''
#Input
'''
5
2 3 6 6 5
'''
#Output
'''
5
'''

if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())
  runnerup_score = sorted(set(arr), reverse=True)[1]
  print(runnerup_score)
#print(list(arr)) : [2, 3, 6, 6, 5]

########################################################################################################################

'''
003 : Finding the percentage
  Score : Half 
  Reason : -
  Topic : dic() 
  Explain : Did not know how to filter in dictionary
'''
#Input
'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''
#Output
'''
56.00
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {} #dictionary
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        #name becomes key, scores become value
    query_name = input()
    #print(student_marks) : {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
    selection = student_marks[query_name]
    # Filter
    total = 0
    # Loop sum
    for i in range(len(selection)):
        total = total+selection[i]
    # 2 digit float
    print("%.2f" % round(total/len(selection), 2))
    
########################################################################################################################

'''
004 : Lists
  Score : Fail 
  Reason : Tried using deque, and tried using nested list, and forgor using int() in every loop
  Topic : list(), if elif
  Explain : Apply if elif in the list
'''
#Input
'''
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
'''
#Output
'''
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    #d= deque()
    d = []
    
    #prompt = []
    for _ in range(N):
        prompt = input().split()
        #prompt.append(action) : This will make nested list 
        if prompt[0] == 'insert':
            d.insert(int(prompt[1]), int(prompt[2]))
        elif prompt[0] == 'remove':
            d.remove(int(prompt[1]))
        elif prompt[0] == 'append':
            d.append(int(prompt[1]))
        elif prompt[0] == 'sort':
            d.sort()
        elif prompt[0] == 'pop':
            d.pop()
        elif prompt[0] == 'reverse':
            d.reverse()
        elif prompt[0] == 'print':
            print(d)
            
    #for i in d: #This is needed almost everytime
    #    print(i,end=" ") 
    
########################################################################################################################
'''
005 : [Coming from Set] Set .discard(), .remove() & .pop()
'''
#Input
'''
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
'''
#Output
'''
4
'''
n = int(input())
s = set(map(int, input().split())) #1 2 3 4 5 6 7 8 9 
''' Only difference from the question above is 's' '''
N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == 'pop':
        s.pop()
    elif order[0] == 'remove':
        s.remove(int(order[1]))
    elif order[0] == 'discard':
        s.discard(int(order[1]))
print(sum(s))

########################################################################################################################
'''
006 : [Coming from Set] Set Mutations
'''
#Input
'''
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
'''
#Output
'''
38
'''
n = int(input())
s = set(map(int, input().split())) '''IMPORTANT : This has to be mapped to create pure set(dictionary form) to work mutation'''
N = int(input())
for i in range(N):
    prompt = input().split()
    element = set(map(int,input().split())) ''' IMPORTANT : Input has to be a pure set form to match with 's' '''
    #print(prompt, element)
    if prompt[0] == 'intersection_update':
        s.intersection_update(element)
    elif prompt[0] == 'update':
        s.update(element)
    elif prompt[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(element)
    elif prompt[0] == 'difference_update':
        s.difference_update(element)
print(sum(s))

########################################################################################################################
'''
007 : [Coming from Collection] Collections.deque()
'''
#Input
'''
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''
#Output
'''
1 2
'''
from collections import deque
d = deque()

for i in range(int(input())):
    c = input().split()
    if c[0]=="append":
        d.append(c[1])
    elif c[0]=="appendleft":
        d.appendleft(c[1])
    elif c[0]=="pop":
        d.pop()
    elif c[0]=="popleft":
        d.popleft()
print(*d)
########################################################################################################################
'''
008 : Climbing the Leaderboard
'''
#Input
'''
7
100 100 50 40 40 20 10
4
5 25 50 120
'''
#Output
'''
6
4
2
1
'''
def climbingLeaderboard(ranked, player):
    scores_set = list(set(ranked))
    scores_set.sort(reverse=True)
    # 100 90 90 80 75 60
    # 100 90 80 75 60
    
    result = []
    l = len(scores_set) #5
    
    for s in player: # 50 65 77 90 10
    
        scores_set.append(s)
        scores_set = list(set(scores_set))
        scores_set.sort(reverse=True)
        
        result.append(scores_set.index(s)+1)
        
    return result
########################################################################################################################

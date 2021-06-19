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

'''
Basic Data Type (Easy ~ Medium)

Find the Runner-Up Score!

#######################################
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
    
    
'''
Basic Data Type (Easy ~ Medium)

Nested Lists

#######################################
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
    
    
'''
Basic Data Type (Easy ~ Medium)

Lists

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

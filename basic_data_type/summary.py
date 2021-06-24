'''
basci_data_types
'''

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
second_highest = sorted(set([score for name, score in ls]))[1]  '''IMPORTANT'''
#print(set([score for name, score in ls])) : {41.0, 37.2, 37.21, 39.0}

print('\n'.join(sorted([name for name, score in ls if score == second_highest])))


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

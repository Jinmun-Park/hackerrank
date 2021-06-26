########################################################################################################################
'''
005 : Find a string
  Score : Success (Must Study Again)
  Reason : Google / Still not understanding
  Topic : while True and string.find()
  Explain : -
'''
#Input
'''
ABCDCDC
CDC
'''
#Output
'''
2
'''
def count_substring(string, sub_string):   
    count = 0
    start = 0
    while True:
        '''IMPORTANT'''
        start = string.find(sub_string, start+1)  #substring index will move (0) (1) (2) 
        if start > 0:
            count+=1
        else:
            return count
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
########################################################################################################################
'''
009 : The Minion Game
  Score : Complete Fail
  Reason : Could not understand logic, only able to build codes after reading discussion
  Topic : Creative loop using +=
  Explain : Find the position of word / Uppercase for the first word only
'''
#Input
'''
BANANA
'''
#Output
'''
Stuart 12
'''
#Explanation
'''
https://www.hackerrank.com/challenges/the-minion-game/problem
'''

def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)): '''IMPORTANT'''
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
            
########################################################################################################################
'''
017: [Coming from Collections]Piling Up!
  Score : Fail
  Reason : Did not understand questions
  Topic : Creative loop()
  Explain : Complicated loop function
'''
#Input
'''
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
'''
#Output
'''
Yes
No
'''
t=int(input()) # t = 2

for _ in range(t):
    n = int(input()) #6
    l = list(map(int, input().split())) #[4, 3, 2, 1, 3, 4] #[1, 3, 2]
    
    if(l[0]==max(l) or l[n-1]==max(l)): # Either
        print("Yes")
    else: 
        print("No")
########################################################################################################################
'''
018: [Coming from Python Functionals]Map and Lambda Function
  Score : Fail
  Reason : fibonacci(n)
  Topic : Complicated loop()
  Explain : Complicated loop function
'''
#Input
'''
5
'''
#Output
'''
[0, 1, 1, 8, 27]
'''
cube = lambda x:x**3 

def fibonacci(n):
    # n = 5
    # fibonacci : [0,1,1,2,3]
    
    a,b = 0,1
    
    for i in range(n):
        ''' IMPORTANT'''
        yield a 
        a,b = b,a+b
            
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
########################################################################################################################
'''
019: [Coming from Python Functionals]Validating Email Addresses With a Filter
  Score : Fail
  Reason : -
  Topic : Filter(), loop()
  Explain : Complicated loop function
'''
#Input
'''
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
'''
#Output
'''
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''
def fun(s):
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    ''' IMPORTANT'''
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))
    # Filter returns filtered value, this returne email that give 'True'

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

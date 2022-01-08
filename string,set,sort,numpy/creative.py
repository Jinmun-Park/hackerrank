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
        '''IMPORTANT : "find(value,start,end)" finds the first occurrence of the specified value.'''
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
015: [Coming from Collections]DefaultDict 
  Score : Complete Fail
  Reason : Did not know using loop insteat of *Count() and *DefaultDict
  Topic : Counter(), for()
  Explain : Incredible!
'''
#Input
'''
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
'''
#Output
'''
1 2 4
3 5
'''
n, m = list(map(int,input().split()))

a=[]
b=[]

for i in range(n):
    a.append(input())
    # a = [a,a,b,a,b]
for j in range(m):
    b.append(input())
    # b = [a,b] imagine b = [a,b,c]
for k in range(len(b)):
    # k = 0,1
    c=[]
    for h in range(len(a)):
     # h = 0,1,2,3,4,5
        if b[k]==a[h]: '''important'''
        # Codintion that has two different iterator. 
        # b[0] = 'a'
        # a[0] = 'a' 
            c.append(h+1) '''important'''
            # h + 1 is required to find the index. range() give from 0, but index should be 1 in the question
    if len(c)>0:
        print(*c)
    else:
        print("-1")
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
    return list(filter(fun, emails)) '''IMPORTANT'''
    # Filter returns filtered value, this returne email that give 'True'

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
########################################################################################################################
'''
020: [Coming from Debugging] Words Score
  Score : Success (Worth studying)
  Reason : -
  Topic : Complex Loop
  Explain : Counter can solve this. Creative !!
'''
#Input
'''
3
programming is awesome
'''
#Output
'''
4
If even +2, odd +1
'''
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words: #programming/is/awesome
        num_vowels = 0
        for letter in word:#p,r,o,g,r,a,m,m,i,ng
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0: # if even
            score += 2
        else:#
            score += 1
    return score

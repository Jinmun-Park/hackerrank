'''
String
'''
'''
Tips 
'''
### STATEMENT 01
string = 'abcde'
substring = 'a'
substring_fail = ['a','e']

# TIPS 01
struig[0] : 'a'
list(string) : ['a', 'b', 'c', 'd', 'e']
string.split() : 'abcde' #By default, space split only
                  
# TIPS 02
string.find(substring) : 0
string.find(substring_fail) : error
                  
# TIPS 03
substring in string : True
substring_fail in string : True 

### STATEMENT 02
from collections import Counter

# TIPS 01
cap_room = Counter(room)
print(*[i for i,v in cap_room.items() if int(v) == 1]) 
                  
# TIPS 02
vowel =['A','E','I','O','U']
S=0
K=0
for i in range(len(string)):
    if string[i] in vowel:
        K+= len(string)-i
    else:
        S+=len(string)-i
                  
# TIPS 03
s = list(map(int, input().split()))
s_count = Counter(s)
for i in range(m):
    customer, price = list(map(int, input().split()))
    if s_count[customer]: #If s_count[*] meets then continue, otherwise False
        total+=price
        s_count[customer]-= 1

########################################################################################################################

'''
summary 
001 : Replacing text at a specific position(Index) we want to put
  - Look at <004 : Mutations>
  - String has to be converted into 'list' before replacing the text(substring) into text
002 : Count sub-string matches with string
  - str.find(sub, start, end) 
  - (start, end) is index position of substring
  - find() returns the index position in string, considering space.
  - find() returns -1, if substring does not match string.
  
 003 : String Validator
  - .isalnum() : alphanumeric/numeric (a-z, A-Z and 0-9).
  - .str.isalpha() : alphabetical (a-z and A-Z)
  - .digits (0-9) : digits
  - .islower()
  - .supper()
  
 004 : Text Wrap (Still not understand)
  - String position in every loop 
  - Loop under df should be pythonic way.
  
'''
########################################################################################################################
'''
001 : sWAP cASE
  Score : success
  Reason : -
  Topic : swap_case() 
  Explain : -
'''
#Input
'''
HackerRank.com presents "Pythonist 2".
'''
#Output
'''
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

########################################################################################################################
'''
002 : String Split and Join
  Score : Success 
  Reason : -
  Topic : - 
  Explain : -
'''
########################################################################################################################
'''
003 : What's Your Name?
  Score : Success 
  Reason : -
  Topic : -
  Explain : -
'''
def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
########################################################################################################################
'''
004 : Mutations
  Score : Half
  Reason : Did not understand changing the list of character before setting the position
  Topic : dictionary
  Explain : Replace Character at Specific Index in String
'''
def mutate_string(string, position, character):
    # string = 'abracadabra' , position = 5, character = 'k'
    string_list = list(string) # Important
    string_list[position]=character
    return "".join(string_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
########################################################################################################################
'''
005 : Find a string
#### MERGED TO 'creative.py' 
'''
########################################################################################################################
'''
006 : Text Wrap
  Score : Half
  Reason : Pythonic way
  Topic : .join()
  Explain : Sting position in every loop 
'''
#Input
'''
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
'''
#Output
'''
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
import textwrap

def wrap(string, max_width):
    return "\n".join(string[i:i+max_width] for i in range(0, len(string), max_width))    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
########################################################################################################################
'''
007 : String Formatting
  Score : Fail
  Reason : Do not understand question
  Topic : .format()
  Explain : number formatting
'''
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i, width=width))
       
########################################################################################################################
'''
008 : Capitalize!
  Score : Half
  Reason : return should contain all loop working in def(). Perfom split in loop.
  Topic : .join()
  Explain : Uppercase for the first word only
'''
def solve(s):
    return ' '.join(w[0].upper() + w[1:] for w in s.split()) #hello world - Hello World / split should be performed in loop
########################################################################################################################
'''
009 : The Minion Game
#### MERGED TO 'creative.py' 
'''
########################################################################################################################
'''
010: Merge the Tools!
#### MERGED TO 'sort.py' 
'''
########################################################################################################################
'''
011: [Coming from Set]The Captain's Room
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
012: [Coming from itertools]Compress the String!
  Score : Failed
  Reason : Did not know how to use Groupby
  Topic : groupby()
  Explain : from itertools import groupby
'''
#Input
'''
1222311
'''
#Output
'''
(1, 1) (3, 2) (1, 3) (2, 1)
'''
from itertools import groupby

sample = input() # 1222311
empty_list = []

for i,c in groupby(sample):
    #print(i, *c) c is set up in the list by default
    #1 1
    #2 2 2 2
    #3 3
    #1 1 1
    c_len = len(list(c)) # list(c) only works for groupby() 
    show = (c_len, int(i))
    empty_list.append(show)
print(*empty_list)
                  

########################################################################################################################
'''
013: [Coming from itertools]Iterables and Iterators
  Score : Half
  Reason : Did not know how to put if function
  Topic : combinations(s,k)
  Explain : from itertools import combination
'''
#Input
'''
4 
a a c d
2
'''
#Output
'''
(1,2)(1,3)(1,4)(2,3)(2,4)(2,3)(3,4)
'''
from itertools import combinations

n =  int(input())
string = input().split()
k = int(input())

comb = list(combinations(string,k))
#print(comb) [('a', 'a'),,,,,,('c', 'd')]
total = len(comb)
sub = len([i for i in comb if 'a' in i]) '''IMPORTANT'''
print(sub/total)
                  
########################################################################################################################
'''
014: [Coming from Collections]collections.Counter()
  Score : Fail
  Reason : Did not know Counter() can use as dictionary method
  Topic : Counter(), for()
  Explain : if s_count[customer]:
'''
#Input
'''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
#Output
'''
200
'''
from collections import Counter

n = int(input())
s = list(map(int, input().split()))
m = int(input())

s_count = Counter(s)
# print(s_count[18]) works. It works because input is listed <s = list(map(int, input().split()))>
total = 0
for i in range(m):
    customer, price = list(map(int, input().split()))
    if s_count[customer]: '''IMPORTANT'''
        #If s_count[*] meets then continue, otherwise False
        total+=price
        s_count[customer]-= 1
    # Counter() returns 0, if s_count[*] does not meet
    # Therefore, it does not need 'else:'
print(total)

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
    
for j in range(m):
    b.append(input())
    
for k in range(len(b)):#k=1,2
    c=[]
    for h in range(len(a)):#h=0,1,2,3,4,5
        if b[k]==a[h]:# b=a,b,(c)
            c.append(h+1) '''important'''
    if len(c)>0:
        print(*c)
    else:
        print("-1")
########################################################################################################################
'''
016: [Coming from Collections]Word Order
  Score : Fail
  Reason : Thought this can only be solved using OrderDictionary
  Topic : OrderDictionary() -> Counter()
  Explain : Counter can solve this. Creative !!
'''
#Input
'''
4
bcdef
abcdefg
bcde
bcdef
'''
#Output
'''
3
2 1 1
'''
from collections import Counter

n = int(input())
list_word = []
for _ in range(n):
    words = input().strip()
    list_word.append(words)

counts = Counter(list_word)
print(len(counts))
print(*counts.values())
########################################################################################################################
'''
017: [Coming from Collections]Piling Up!
#### MERGED TO 'creative.py' 
'''
########################################################################################################################
'''
018: [Coming from Python Functionals]Map and Lambda Function
#### MERGED TO 'creative.py' 
'''
########################################################################################################################
'''
019: [Coming from Python Functionals]Validating Email Addresses With a Filter
#### MERGED TO 'creative.py' 
'''
########################################################################################################################
'''
020: [Coming from Debugging] Words Score
#### MERGED TO 'creative.py' 
'''
########################################################################################################################


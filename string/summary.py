'''
String
'''
'''
Tips 
'''
# STATEMENT
string = 'abcde'
substring = 'a'
substring_fail = ['a','e]

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
# TIPS 04



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
  Topic : Replace Character at Specific Index in String
  Explain : -
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
  Score : Success (Must Study Again)
  Reason : Google / Still not understanding
  Topic : - 
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
006 : Text Wrap
  Score : Half
  Reason : Pythonic way
  Topic : Sting position in every loop 
  Explain : -
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
  Topic : number formatting
  Explain : -
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
  Topic : Uppercase for the first word only
  Explain : -
'''
def solve(s):
    return ' '.join(w[0].upper() + w[1:] for w in s.split()) #hello world - Hello World / split should be performed in loop
########################################################################################################################
'''
009 : The Minion Game
  Score : Complete Fail
  Reason : Could not understand logic, only able to build codes after reading discussion
  Topic : Uppercase for the first word only
  Explain : Find the position of word
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
    for i in range(len(string)):
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
010: Merge the Tools!
#### Look at 011: [Coming from Set]The Captain's Room
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
    # your code goes here      
    for i in range(0,len(string),k):
        sort = sorted(set(string[i:i+k]), key = string[i:i+k].index)
        print(''.join(sort))
########################################################################################################################
'''
011: [Coming from Set]The Captain's Room
  Score : Success
  Reason : 
  Topic : Count()
  Explain : Count unique characted
'''
#Input
'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
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
  Topic : from itertools import groupby 
  Explain : groupby
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
    c_len = len(list(c))
    show = (c_len, int(i))
    empty_list.append(show)
print(*empty_list)
                  
#print(i, *c) c is set up in the list by default
#1 1
#2 2 2 2
#3 3
#1 1 1

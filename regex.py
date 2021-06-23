############################################################################################################# IMPORTANT
# re (match)
'''
Regex and Parsing
Detect Floating Point Number

Sample Input
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output
False
True
True
False

*Number can start with +, - or . symbol
*Number must contain at least 1 decimal value.
*Number must have exactly one . symbol.
*Number must not give any exceptions when converted using float(N)
'''
import re

class Main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))

'''r'^[-+]?[0-9]*\.[0-9]+$''''
# {} : Number of occurences
# ^ : Start
# & : End 
# ? : ab? will match either ‘a’ or ‘ab’
# \1 : same pattern
# \d = Returns a match where the string contains digits
# [-+]? : ab? will match either ‘a’ or ‘ab’
# [0-9]* : ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
# \ : Signals a special sequence (can also be used to escape special characters)
# . : In the default mode, this matches any character except a newline
# [0-9]+ : ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
 
'''m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')'''
# m.group(0) : 'username@hackerrank.com'
# m.group(1) : 'username'
# \w : returns a match where the string contains any word characters    
# + : one or more occurrences

'''pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"'''
'''bool(re.match(pattern, email))'''
# + : one or more occurrences
# \. : Signals '.'
# {1,2,3} : 1 to 3 extension

'''re.findall(r'\w','http://www.hackerrank.com/')'''
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# re.findall() returns all the non-overlapping matches of patterns

'''re.finditer(r'\w','http://www.hackerrank.com/')'''
# map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

'''print(re.sub(r"(?<= )(\|\||&&)(?= )", change, input()))'''
# | : Either or	
# \ : Signals a special sequence

'''r"([a-zA-Z0-9])\1+"'''
# ([a-zA-Z0-9]) lowercase letter, uppercase letter, or digit
# 1+ : 1 occurence

'''r"^[789]\d{9}$"'''
# any 9 occurenes after 7,8,9 at the first
'''r"^[1-9][\d]{5}$"'''
# 1~9 at the first, then 1~9 in 5 occurences

''' not re.search(r'(\d)\1{3,}'''' 
# It must not have 4 or more consecutive pattern
'''a = r"(\d)(?=\d\1)"
len(re.findall(a, P)) < 2)
'''
# not contain more than one alternating repetitive digit pair

if __name__ == '__main__':
    obj = Main()
############################################################################################################# 
# re (match)
'''
Sample Input
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output
DEXTER <dexter@hotmail.com>

The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.
'''
import re

N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)
############################################################################################################# IMPORTANT
# re (match)
# not re.search(r'(\d)\1{3,}' : must not have 4 or more consecutive pattern
# \1 means same pattern
'''
Validating Credit Card Numbers

Sample Input
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output
Valid
Valid
Invalid
Valid
Invalid
Invalid

'''
import re
t = int(input().strip())

for _ in range(t):
    num = "".join(input()) #Not so special 
    if (re.match(r'^[456]', num) and # start with 4 or 5 or 6
        (re.match(r'([\d]{4}-){3}[\d]{4}$', num) or re.match(r'[\d]{16}', num)) and # must 16 digitss, and '-' in every 4 digit
        not re.search(r'(\d)\1{3,}', num.replace("-", ""))): # must not have 4 or more consecutive pattern after removing '-'
        print("Valid")
    else:
        print("Invalid")
############################################################################################################# 
# re (match, findall)
# r"^[1-9][\d]{5}$" : 1~9 at the first, then 1~9 in 5 occurences
# r"(\d)(?=\d\1)" : not contain more than one alternating repetitive digit pair
'''
Validating Postal Codes

Sample Input
110000

Sample Output
False

 must be a number in the range from  100000 to 999999 inclusive.
 must not contain more than one alternating repetitive digit pair.
'''
regex_integer_in_range = r"^[1-9][\d]{5}$"   
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"   

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
############################################################################################################# 
# email (but not using re)
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
        username, url = s.split('@')
        website,extension = url.split('.')
    except ValueError:
        return False
    
    if username.replace('-','').replace('_','').isalnum() is False: # if true then true
        return False
    
    elif website.isalnum() is False:
        return False
    
    elif len(extension) > 3:
        return False
    
    else :
        return True
    
def filter_mail(emails):
    return list(filter(fun, emails)) # filter shows only true value

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
#############################################################################################################
# decoration (but not using re / sorted)
'''
Closures and Decorators
Standardize Mobile Number Using Decorators

Sample Input 0
3
07895462130
919875641230
9195969878

Sample Output 0
+91 78954 62130
+91 91959 69878
+91 98756 41230

Explanation
The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.
'''
def wrapper(f):
    def fun(l):
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#############################################################################################################
# decoration (but not using re / sorted)
'''
Closures and Decorators
Decorators 2 - Name Directory

Sample Input 0
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output 0
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle

Explanation
Print their names in a specific format sorted by their age in ascending order '''

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#############################################################################################################
# re (sub)
# re.sub() tool evaluates a pattern and, for each valid match, it calls a method (or lambda)
# \d = Returns a match where the string contains digits

'''Transformation of String'''
import re
def square(match):
    number = int(match.group(0))
    return str(number**2)
print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9") 
#############################################################################################################
# re (sub)
# *? : it means match the previous element as few times as possible

'''Replacements in Strings'''
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""
print re.sub("(<!--.*?-->)", "", html)  

<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
############################################################################################################# IMPORTANT
# re (sub)
# | : Either or	
# \ : Signals a special sequence
''' INPUT
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
'''

''' OUTPUT
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides. 
'''

import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change, input())) 

#############################################################################################################
# re (findall) : The findall() function returns a list containing all matches.
# r"^[789]\d{9}$" : ^[789] : starts with any number among 7,8,9
# r"^[789]\d{9}$" : \d{9}$ : 9 digits after ^[789]
# \d = Returns a match where the string contains digits
# {}  = number of occurence
'''
Regex and Parsing
Validating phone numbers

Sample Input    
2
9587456281
1252478965

Sample Output
YES
NO

A valid mobile number is a ten digit number starting with a  7,8, or 9.

'''

import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)  
        if(len(output)==1): 
            # if return is 1 list, then its Okay. If return more than 1, then its no.
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
#############################################################################################################
# re (findall) : The findall() function returns a list containing all matches.
# qwrtypsdfghjklzxcvbnm = consonants
# aeiou = vowel
# ?<= : (?<=a)b (positive lookbehind) matches the b (and only the b) in cab
# ?=  : Positive lookahead works just the same. q(?=u) matches a q that is followed by a u
'''
Regex and Parsing
Re.findall() & Re.finditer()

Sample Input    
rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output
ee  
Ioo
Oeo
eeeee

These substrings must lie in between 2 consonants and should contain vowels only.
ee is located between consonant d and f.
'''
import re

Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)
#############################################################################################################
# re (search)
# ([a-zA-Z0-9]) lowercase letter, uppercase letter, or digit
# 1+ : 1 occurence
'''
Regex and Parsing
Group(), Groups() & Groupdict()

Sample Input    
..12345678910111213141516171820212223

Sample Output
1

Your task is to find the first occurrence of an alphanumeric character in text (read from left to right) that has consecutive repetitions.
'''
import re
expression=r"([a-zA-Z0-9])\1+"
m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)
#############################################################################################################
# re (search)
'''
Regex and Parsing
Validating UID

Sample Input    
2
B1CD102354
B1CDEF2354

Sample Output
Invalid
Valid

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''
import re
for _ in range(int(input())):
    uid = input()
    uid = "".join(sorted(uid)) # This must be included
    if (re.search(r"[A-Z]{2}",uid) and #2 uppercase alphabets
        re.search(r"\d{3}",uid) and #3+ digits
        not re.search(r"[^A-Za-z0-9]",uid) and #no nonalphanumeric
        not re.search(r"(\w)\1",uid) and #no repetition
        len(uid) == 10): #10 characters long
        print("Valid")
    else:
        print("Invalid")
#############################################################################################################
# re (compile, search)

'''
Regex and Parsing
Re.start() & Re.end()

Sample Input    
aaadaa
aa

Sample Output
(0, 1)  
(1, 2)
(4, 5)
'''
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
#aaadaa
#aa

if not match: 
    print('(-1, -1)')
    
while match is not None:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)
    
'''
More infor about while function : https://www.tutorialspoint.com/python/python_while_loop.htm
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
'''
############################################################################################################# 
# re (compile)
# Compile a regular expression pattern into a regular expression object
'''
Errors and Exception
Incorrect Regex

Sample Input
2
.*\+
.*+

Sample Output
True
False
'''
import re;

N = int(input())
for _ in range(N):
    try:
        re.compile(input()) 
        Output = True
    except re.error:
        Output = False
    
    print(Output)
#############################################################################################################
# re (split)
# [.,] '.',',' includes within bracket. These words will be splited
'''
Regex and Parsing
Re.split()

Sample Input
100,000,000.000

Sample Output
100
000
000
000
'''
regex_pattern = r"[.,]+"

import re
print("\n".join(re.split(regex_pattern, input())))
#############################################################################################################

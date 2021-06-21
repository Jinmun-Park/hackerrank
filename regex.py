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

# {} : Number of occurences
# ^ : Start
# & : End 
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

'''re.findall(r'\w','http://www.hackerrank.com/')'''
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# re.findall() returns all the non-overlapping matches of patterns

'''re.finditer(r'\w','http://www.hackerrank.com/')'''
# map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

'''print(re.sub(r"(?<= )(\|\||&&)(?= )", change, input()))'''
# | : Either or	
# \ : Signals a special sequence

if __name__ == '__main__':
    obj = Main()
############################################################################################################# 
# re (sub)
# re.sub() tool evaluates a pattern and, for each valid match, it calls a method (or lambda)

'''Transformation of String'''
import re
def square(match):
    number = int(match.group(0))
    return str(number**2)
print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9") 
# \d = Returns a match where the string contains digits
#############################################################################################################
# re (sub)
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
# *? : it means match the previous element as few times as possible

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
# | : Either or	
# \ : Signals a special sequence
#############################################################################################################
# re (findall)
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
# r"^[789]\d{9}$" : ^[789] : starts with any number among 7,8,9
# r"^[789]\d{9}$" : \d{9}$ : 9 digits after ^[789]
# \d = Returns a match where the string contains digits
# {}  = number of occurence
import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)  # []
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
#############################################################################################################
# re (findall)
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
# qwrtypsdfghjklzxcvbnm = consonants
# aeiou = vowel
# ?<= : (?<=a)b (positive lookbehind) matches the b (and only the b) in cab
# ?=  : Positive lookahead works just the same. q(?=u) matches a q that is followed by a u

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)
#############################################################################################################
# re (search)
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
expression=r"([a-zA-Z0-9])\1+" # ([a-zA-Z0-9]) lowercase letter, uppercase letter, or digit
m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)
#############################################################################################################
# re (split)
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
regex_pattern = r"[.,]+" # [.,] '.',',' includes within bracket. These words will be splited

import re
print("\n".join(re.split(regex_pattern, input())))
############################################################################################################# 
# re (compile)
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
        re.compile(input()) # Compile a regular expression pattern into a regular expression object
        Output = True
    except re.error:
        Output = False
    
    print(Output)
#############################################################################################################

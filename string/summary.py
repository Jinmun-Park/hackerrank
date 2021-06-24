'''
String
'''

'''
summary 
001 : Replace Character at Specific Index in String
  - Look at <004 : Mutations>
  - Convert list before changing the text

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
  
 004 : Text Wrap 
  - Sting position in every loop 
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
  Score : Success
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
    return "\n".join(string[i:i+max_width]for i in range(0, len(string), max_width))    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
########################################################################################################################

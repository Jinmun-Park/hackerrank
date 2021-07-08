'''
Name : [Implementation]Modified Kaprekar Numbers
Level : Easy 
Topic 001 : Loop () and if()
Topic 002 : String Sequence

Input : 
STDIN   Function
-----   --------
1       p = 1
100     q = 100

Output : 
1 9 45 55 99

Description : 
n=5 and d=1, first square n, that would be 25. Then we split digit and sum it. The sum of value, 7, should be equal to n, 5.
If n=45, square value is 2025. 20 + 25 equals to 45.
'''

def kaprekarNumbers(p, q):
    numlist = []
    for i in range(p, q + 1):
        if i == 1:
            numlist.append(i)
        elif i**2 > 9:
            numstring = str(i**2)
            rem = len(str(numstring)) - len(str(i)) '''IMPORTANT'''
            left = numstring[:rem]
            right = numstring[rem::]
            if int(left) + int(right) == i:
                numlist.append(i)
    
    if len(numlist) == 0:
        print("INVALID RANGE")
    else:
        for i in range(len(numlist)):
            print(numlist[i], end = ' ')

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)






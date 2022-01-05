# STATEMENT
# TIPS 01


'''
summary 
001 : 
  
'''
########################################################################################################################
'''
001 : Diagonal Difference
  Topic : 
  Explain : 
'''

#Input
'''
3
11 2 4
4 5 6
10 8 -12
'''

#Output
'''
15
'''

def diagonalDifference(arr):
    n = len(arr)
    left = 0
    right = 0

    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-i-1]

    return abs(left - right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    #[[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

########################################################################################################################

'''
002 : Apple and Orange
  Topic : 
  Explain : 
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))

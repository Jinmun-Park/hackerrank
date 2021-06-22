# numpy.set_printoptions(legacy='1.13')
########################################################################################################
# Numpy (loop understanding)
# Putting input() into array
'''
Numpy
Min and Max

Input
4 2
2 5
3 7
1 3
4 0

Output
3
'''
import numpy 
N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))
########################################################################################################
# Numpy 
'''
Numpy
Mean, Var, and Std

Input
2 2 #n, m
1 2
3 4

Output
[ 1.5  3.5] # axis 1
[ 1.  1.]
1.11803398875
'''
import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
print(A.std())
########################################################################################################
# Numpy [::-1] refers to reverse and float
'''
Numpy
Arrays

Input
1 2 3 4 -8 -10

Output
[-10.  -8.   4.   3.   2.   1.]
'''
import numpy

def arrays(arr):
    arr = numpy.array(arr[::-1], float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
########################################################################################################
# Numpy Reshape
'''
Numpy
Shape and Reshape

Input
1 2 3 4 5 6 7 8 9

Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 '''
import numpy
array = numpy.array(input().split(), int)
print(numpy.reshape(array, (3,3)))
########################################################################################################
# Numpy Tranpose/Flatten
# Transpose : numpy.transpose(a)
# Flatten : a.flatten()
my_array = numpy.array([[1,2,3],[4,5,6]])
print numpy.transpose(my_array)
''' [[1 4] [2 5] [3 6]]'''

my_array = numpy.array([[1,2,3],[4,5,6]])
print my_array.flatten()
'''[1 2 3 4 5 6]'''

########################################################################################################
# Numpy Concatenate (Change axis=0 or axis=1 if you have error)
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])
print numpy.concatenate((array_1, array_2, array_3))   
'''[1 2 3 4 5 6 7 8 9]'''

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print numpy.concatenate((array_1, array_2), axis = 1) 
'''[[1 2 3 0 0 0]
 [0 0 0 7 8 9]] '''

array_concatenate = numpy.concatenate((a, b), axis=0)
'''[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] '''
########################################################################################################
# Numpy Zeros and Ones (Tuple)
# print(numpy.zeros(N, int)) : by default, it will be float

'''
Input
3 3 3

Output
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''
import numpy

N = tuple(map(int, input().split()))
#(3, 3, 3)

print(numpy.zeros(N, int))
print(numpy.ones(N, int))
########################################################################################################
# Numpy Eye and Identity 
'''
Input
3 3

Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''
print(numpy.eye(*map(int, input().split())))
########################################################################################################
# Numpy Array Math
N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B) #Division 
print(A % B) #Mod
print(A ** B) #Power
########################################################################################################
# Numpy Ceil/Rint
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)         
'''[  2.   3.   4.   5.   6.   7.   8.   9.  10.]'''
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          
'''[  1.   2.   3.   4.   6.   7.   8.   9.  10.]'''
########################################################################################################
# Numpy Product
'''
INPUT
2 2
1 2
3 4
OUTPUT
24
(1+3)*(2+4) : axis = 0
'''
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))
########################################################################################################
# Numpy Inner,Outer (Check Dot,Cross for matrix product)
# Inner : (0*2)+(1*3)
'''
Input
0 1
2 3
Output
3
[[0 0]
 [2 3]]
'''
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')
########################################################################################################
# Numpy Polynomial
'''
Input
1.1 2 3
0
Output
3.0
'''
poly = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(poly, x))
########################################################################################################
# Linear Algebra (linalg.det, linalg.eig, linalg.inv)
'''
Input
2
1.1 1.1
1.1 1.1
Output
0.0
'''
import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(round(numpy.linalg.det(A),2))

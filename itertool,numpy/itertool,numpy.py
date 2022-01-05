'''
itertools & Numpy
'''
'''
Tips 
'''
# STATEMENT
from itertools import combinations

# TIPS 01
print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]

# TIPS 02
print permutations(['1','2','3'])
'''<itertools.permutations object at 0x02A45210>'''
print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

# TIPS 03
arr = numpy.array(l)
'''
[[1 2]
[3 4]]
'''
tr_arr = numpy.transpose(arr)
'''
[[1 3]
[2 4]]
'''
fl_arr = arr.flatten()
'''[1 2 3 4]'''

# TIPS 04
my_array = numpy.array([ [1, 2], [3, 4] ])
print numpy.sum(my_array, axis = 0)         #Output : [4 6] : (1+3)+(2+4)
print numpy.sum(my_array, axis = 1)         #Output : [3 7] : (1+2)+(3+4)
print numpy.sum(my_array, axis = None)      #Output : 10

# TIPS 05
my_array = numpy.array([[2, 5], [3, 7],[1, 3],[4, 0]])
print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]

# TIPS 06
print numpy.mean(my_array, axis = 0)
print numpy.var(my_array, axis = 0)  
print numpy.std(my_array, axis = 0)
########################################################################################################################
'''
001: [Coming from Numpy]Transpose and Flatten
  Score : Success
  Reason : 
  Topic : Numpy()
  Explain : -
'''
#Input
'''
2 2
1 2
3 4
'''
#Output
'''
[[1 3]
 [2 4]]
[1 2 3 4]
'''
import numpy

n, m = input().split()
l = []

for i in range(int(n)):
    l.append(list(map(int,input().split())))
    # array is important to make your input() to be in the 'list'

arr = numpy.array(l)
print(arr) 
#[[1 2]
#[3 4]]

tr_arr = numpy.transpose(arr)
print(tr_arr)
#[[1 3]
# [2 4]]

fl_arr = arr.flatten()
print(fl_arr)
#[1 2 3 4]
########################################################################################################################

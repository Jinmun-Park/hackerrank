'''
Class
Classes: Dealing with Complex Numbers

Sample Input
2 1
5 6

Sample Output
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i

Explanation
For complex numbers with non-zero real (A) and complex part (B), the output should be in the following format:
A + Bi
Replace the plus symbol (+) with a minus symbol (-) when B < 0.
For complex numbers with a zero complex part i.e. real numbers, the output should be:
A + 0.00i
For complex numbers where the real part is zero and the complex part is non-zero, the output should be:
0.00 + Bi
'''

import math
     
class Complex(object):
# Classes Dealing with Complex Numbers in python - Hacker Rank Solution START
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real,imaginary)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real,imaginary)
        
    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real,imaginary)

    def __truediv__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * Complex(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real) # Real number = 0 (A + 0.00i) (%.2f means 2 float digits)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary) # (A + Bi)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary)) # where the real part is zero and the complex part is non-zero
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))  # when B < 0 (A + Bi) 
        return result #print(*) means more than 1
    
        
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

################################################################################################################################################################
'''
Class
Class 2 - Find the Torsional Angle

Sample Input
0 4 5
1 7 6
0 5 9
1 7 2

Sample Output
8.19
'''

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return Points(x, y, z)

    def dot(self, no):
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split())) # x, y, z list 
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3]) #a = [0,4,5] / [1,7,6]
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
################################################################################################################################################################
'''
Debugging
Default Arguments

Sample Input
3
odd 2
even 3
odd 5

Sample Output
1
3
0
2
4
1
3
5
7
9

Explanation

'''

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None): 
#def print_from_stream(n, stream=EvenStream()): This does make EvenStream default
    if stream is None: # you have to se this to make the function works
        stream = EvenStream()
        
    for _ in range(n):
        print(stream.get_next())
        


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())


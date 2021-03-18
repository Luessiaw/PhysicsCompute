'''临时需要的一些函数'''

from math import *
from mathFunc import *

def funcA(x):
    even_x = even(x)
    s0 = 0.51/sqrt(3)
    s1 = randomError(x)
    s = sss([s0,s1])
    print(even_x)
    print(1/even_x**2)
    print(2/even_x**3*s)

def funcB(r,x):
    even_x = even(x)
    s0 = 0.51/sqrt(3)
    s1 = randomError(x)
    s_t = sss([s0,s1])
    s_r = 0.1/sqrt(3)
    s = sss([2/even_x*s_t,s_r/r])/even_x**2/r
    print(even_x)
    print(1/even_x**2/r)
    print(s)
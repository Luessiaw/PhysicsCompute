from math import *


def alter(x):
    if type(x[0]) in [list,tuple]:
        x = x[0]
    return x

def even(*x):
    '''求平均值。x: a list of numbers.'''
    x = alter(x)
    return sum(x)/len(x)

def liner(x,y):
    '''最小二乘法，返回斜率和截距。x,y: lists of numbers, of the same length.'''
    even_x = even(x)
    even_y = even(y)
    upper = sumXY(x,y)
    lower = sumXY(x,x)
    k = upper/lower
    b = even_y-even_x*k
    print('y=kx+b\n',k,b)
    return k,b

def variance(*x):
    '''方差. x: a list of numbers.'''
    x = alter(x)
    n = len(x)
    return sqrt(sumXY(x,x)/n)

def sss(*x):
    '''sqrt_sum_squared, 求平方和的平方根。'''
    x = alter(x)
    return sqrt(sum([_x**2 for _x in x]))

def ssd(*x):
    '''sum_squared_difference 求与平均值的差的平方和'''
    x = alter(x)
    return sumXY(x,x)

def zhuCha(*x):
    '''逐差法返回差值列表'''
    x = alter(x)
    n = len(x)
    x1 = x[:n//2]
    x2 = x[n//2:]
    return [_[1]-_[0] for _ in zip(x1,x2)]

def reduceSum(*x):
    '''求部分和'''
    x = alter(x)
    return [sum(x[:i+1]) for i in range(len(x))]

def randomError(*x):
    '''随机误差造成的不确定度'''
    x = alter(x)
    n = len(x)
    return variance(x)/sqrt(n-1)

def sumXY(x,y):
    '''向量的乘积再减去平均值乘积的n倍。'''
    return sum([_x*_y for (_x,_y) in zip(x,y)])-len(x)*even(x)*even(y)

def personR(x,y):
    '''Person Correlation Coefficient, 皮尔逊相关系数'''
    return sumXY(x,y)/sqrt(sumXY(x,x)*sumXY(y,y))



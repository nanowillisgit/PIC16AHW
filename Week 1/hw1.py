#!/usr/bin/env python
"""
Created on Thurs Oct 8

@author: Aatmun Baxi
"""
#%%
"""
Submission for homework 1
"""

import random
from random import randint

def largerIndex(c):
    """
    Accepts list c and returns array of -1,0,1 depending on if the elements of c are less than, equal to, or greater than the element's index, respectively
    input c: Array to be analyzed
    return: Array whose values reflect the inequality relationships described above
    """

    k = [0] * len(c)

    ### Load array according to leq, eq, geq, schema
    for i in range(len(c)):
        if c[i] == i:
            k[i] = 0
        elif c[i] > i:
            k[i] = 1
        else:
            k[i] = -1
    return k

def squareUpTo(n):
    """
    Accepts integer n and returns array of square numbers less than or equal to n
    input n: int
    return: array of squares less than or equal to n
    """
    max = 1

    ### Find upper bound of square-able integer
    while max**2 <= n:
        max +=1

    ### Return all squares less than upper bound
    return [ i**2 for i in range(max)]

#print(squareUpTo(9))

def fliplin3():
    """
    Biased coin made up of unbiased processes
    return: boolean of coin flip
    """

    ### 2-element list with 2 random values
    event_array = [ random.randint(0,1) for i in range(2) ]

    ### Sum determines the result of flip
    result = sum(event_array)

    ### Return bool unfairly based on list sum
    if result == 1:
        return False
    elif result == 2:
        return True
    else:
        return fliplin3()
        

def duplicates(c):
    """
    Returns list of duplicate elements in input list, preserving order

    input c: list
    return: list of duplicate elements
    """
    ### Load all instances of duplicated in new list
    dup = [ i for i in c if ( c.index(i) != len(c) - 1 - list(reversed(c)).index(i) )]

    bare = []

    ### Load new values from duplicate instances, without repeats
    [ bare.append(x)  for x in dup if x not in bare ]
    return bare

l1 = [1,2,0,4,2,1,40,-5]
l2 = [0,3,2,1,32,3,4,0]
print(largerIndex(l1))
print(largerIndex(l2))


#l3 = [1,2,5,3,6,2,4,5,5,5,5,5]
#l4 = [1,3,5,5,1,4,3]

#print(duplicates(l3))
#print(duplicates(l4))

bool_array = []
for i in range(10000):
    bool_array.append( fliplin3() )

print("Success count: " , bool_array.count(True) / len(bool_array))
print("Fail count: ", bool_array.count(False) / len(bool_array) )

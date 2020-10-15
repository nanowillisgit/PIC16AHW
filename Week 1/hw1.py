#!/usr/bin/env python
"""
Created on Thurs Oct 8

@author: Aatmun Baxi
"""
#%%
"""
Submission for homework 1
"""
import math
import random
from random import randint


def largerIndex(c):
    """
    Accepts list c and returns array of -1,0,1 depending on if the elements of c are less than, equal to, or greater than the element's index, respectively

    input c (list): list to be analyzed

    return (list): list whose values reflect the inequality relationships described above
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

    input n (int): max int for output list

    return (list): list of squares less than or equal to n
    """
    ### Return all squares less than upper bound
    return [ i**2 for i in range( math.floor(math.sqrt(n)) +1 ) ]


def fliplin3():
    """
    Biased coin made up of unbiased processes

    return (bool): boolean of coin flip
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

    input c (list): list to be analyzed

    return (list): list of duplicate elements
    """
    ### Load all instances of duplicated in new list
    ##### Determined based on whether the first appeareance of
    ##### the element's index matches that index when searching
    ##### the list backwards subtracted from the total list length
    ### Duplicates are loaded as many times as they appear 
    dup = [ i for i in c if ( c.index(i) != len(c) - 1 - list(reversed(c)).index(i) ) ]

    bare = []

    ### List stripped of duplicates of duplicates
    [ bare.append(x)  for x in dup if x not in bare ]
    return bare

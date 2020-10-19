#!/usr/bin/env python3

from math import exp, sin, cos


def traversal_length(d,k,visited,length):
    """
    Traverses a dictionary through path and returns length

    Params
    -------------------------
    d (dictionary): dictionary to traverse
    k (key of d): key to start traversal from
    visited (list): list of keys already visited in path
    length (int): length of path already traversed

    Return
    -------------------------
    length: length of path traversed
    """

    # If key visited return length
    if k in visited:
        return length-1

    # Get value associated to key
    new = d.get(k)

    # If value also a key...
    if new in d.keys():

        # Append key to visited
        visited.append(k)

        # Recurse starting from the key equal to old key's value
        return traversal_length(d,new,visited,length+1)
    # Else value not a key, path terminated
    else:
        return length

def longestpath(d):
    """
    Gets longest path in dictionary

    Params
    -------------------------
    d (dictionary): dictionary to get path length from
    """

    # If d empty no path length
    if not d:
        return 0

    path_lengths = []

    # For each key in d, measure path
    for key in d.keys():
        path_lengths.append( traversal_length(d,key,[],1) )

    # Return max of path lengths
    return max(path_lengths)

#d1 = {"a":"b","b":"c"}
#d3 = {}
#d2 = {"b":"c"}
#d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}
#print(longestpath(d1))




def solve( f, gs, tol):
    if abs( f(gs)[0] ) <= tol:
        return gs
    else:
        try:
            return solve(f, gs - ( f(gs)[0] / f(gs)[1] ),tol)
        except ZeroDivisionError as ze:
            return "zero division error", ze

print(solve(lambda x: [x**2-1, 2*x], 3, 0.0001))
print(solve(lambda x: [x**2-1, 2*x], -1, 0.0001))
print(solve(lambda x: [exp(x)-1, exp(x)], 1, 0.0001))
print(solve(lambda x: [sin(x), cos(x)], 0.5, 0.0001))


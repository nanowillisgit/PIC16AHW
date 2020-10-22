#!/usr/bin/env python3

from math import exp, sin, cos

def traversal_length(d, k , visited = [],length = 0):
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

    # If key visited return length (compensated for +1 in function call)
    if k in visited:
        return length-1

    # Get value associated to current key
    new = d.get(k)

    # If value also a key...
    if new in d.keys():

        # Append key to visited keys
        visited.append(k)

        # Recurse starting from the key equal to old key's associated value
        return traversal_length(d,new,visited,length+1)

    # Else value not a key, terminate path
    else:
        return length

def longestpath(d):
    """
    Gets longest path in dictionary

    Params
    -------------------------
    d (dictionary): dictionary to get path length from

    Return
    -------------------------
    Length of longest path
    """

    # If d empty no path length
    if not d:
        return 0

    path_lengths = []

    # For each key in d, measure path
    for key in d.keys():
        path_lengths.append( traversal_length( d, key, [], 1 ) )

    # Return max of path lengths
    return max(path_lengths)

# d1 = {"a":"b","b":"c"}
# d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}
# d3 = {"a":"b", "b":"c", "c":"d", "z":"h", "h":"g" ,"g":"e", "e":"a", "f":"a", "d":"b"}
# print("d1:", longestpath(d1))
# print("d2:", longestpath(d2))
# print("d3:", longestpath(d3))

def solve( f, gs , tol = 0.0001):
    """
    Numerically solves for root using Newtons method

    Params
    ---------------------------------------------
    f (lambda returning list of [ value and derivative ]): lambda of function and derivative
    gs (num): initial root guess to start iteration from
    tol (num) = 0.0001: Acceptable error tolerance for guess

    Returns
    ---------------------------------------------
    Numerically calculated root
    """
    # Base case: within error tolerance
    if abs( f(gs)[0] ) <= abs(tol):
        return gs
    # Else try to continue
    else:
        try:
            return solve(f, gs - ( f(gs)[0] / f(gs)[1] ), tol)
        # Throw exception if f'(x_n)=0
        except ZeroDivisionError as ze:
            return "zero division error", ze

# print(solve(lambda x: [x**2-1, 2*x], 3, 0.0001))
# #  Result: 1.0000305180437934

# print(solve(lambda x: [x**2-1, 2*x], -1, 0.0001))
# #  Result: -1

# print(solve(lambda x: [exp(x)-1, exp(x)], 1, 0.0001))
# #  Result: 1.5641107898984284e-06

# print(solve(lambda x: [sin(x), cos(x)], 0.5, 0.0001))
# #  Result: 3.311802132639069e-05

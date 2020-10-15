#!/usr/bin/env python3

import hw1
import random
from random import randint

l1 = [1,2,0,4,2,1,40,-5]
#l2 = [0,3,2,1,32,3,4,0]
l2 = [0,1,2,1,32,3,4,0]

print(hw1.largerIndex(l1))
print(hw1.largerIndex(l2))
#print(hw1.largerIndex([]))

print(hw1.squareUpTo(10))
print(hw1.squareUpTo(100))

flips = [ hw1.fliplin3() for i in range(100000) ]

print("True:", flips.count(True) / len(flips))
print("False:", flips.count(False) / len(flips))

l3 = [1,2,5,3,6,2,4,5]
l4 = [1,3,5,5,1,4,3]

print(hw1.duplicates(l3))
print(hw1.duplicates(l4))

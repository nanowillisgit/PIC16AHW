#!/usr/bin/env python3
import math

list = [ x for x in range(99,10002) if ( math.sqrt(x) - math.floor( math.sqrt(x)) == 0) ]
#print(list)

print(sum(list))


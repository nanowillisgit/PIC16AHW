# -*- coding: utf-8 -*-
"""
Hw3 test code
2020 Fall PIC 16 A
"""
from hw3 import Node, LinkedList

a = LinkedList(0)
a.append(1)
a.append(2)

print("7 points if this works")
for n in a:
    print(n)

print("")

print("2 points if this works")
for n in a:
    print(n)

print("")

print("3 points if both of these work")
for n in a:
    if n == 2:
        break
    else:
        print(n)

print("")
   
for n in a:
    if n == 2:
        break
    else:
        print(n)

print("")

a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)

print("")

print("1 points if this works")
print(len(a))
print("")

print("1 points if this works")
print(str(a))
print("")

print("1 points if this works")
print(repr(a))
print("")


print("1 points each. That is, 2 points if the output of the next line is correct")
a[5] = 20
print(a[5])

print("")

print("2 points for correct operation of +")
a+9 # doesn't modify a
print(a)

print("")

a = a+9 # appends 9 to a
print(a)


print("")

print("1 points for raising correct IndexError")
try:
    print(a[999])
except IndexError as e:
    print(e)

print("")


print("")
print("-----")
print("")
print("Example output:")
print("""
7 points if this works
0
1
2

2 points if this works
0
1
2

3 points if both of these work
0
1

0
1


1 points if this works
9

1 points if this works
[0->1->2->3->4->5->6->7->8->]

1 points if this works
'[0->1->2->3->4->5->6->7->8->]'

1 points each. That is, 2 points if the output of the next line is correct
20

2 points for correct operation of +
[0->1->2->3->4->20->6->7->8->]

[0->1->2->3->4->20->6->7->8->9->]

1 points for raising correct IndexError
list index out of range

""")

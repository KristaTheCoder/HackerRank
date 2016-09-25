#!/bin/python

import sys

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice = [a0, a1, a2]
bob = [b0, b1, b2]
a = 0 
b = 0
for i in range(len(alice)):
    if alice[i] > bob[i]:
        a += 1
    elif alice[i] < bob[i]:
        b = b + 1
   
print a, b

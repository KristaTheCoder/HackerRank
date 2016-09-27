#!/bin/python

import sys


n = int(raw_input().strip())
numSpace = n
numHash = 1
while(numSpace >= 0):
    for i in range(numSpace):
        print "",
    for i in range(numHash):
        print "#"
    numSpace = numSpace - 1
    numHash = numHash + 1
    

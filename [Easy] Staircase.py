#!/bin/python

import sys

n = int(raw_input().strip())
numSpace = n
numHash = 1
while(numSpace > 0):
    for i in range(numSpace):
        print '',
    for i in range(numHash):
        sys.stdout.write("#"), #Needs comma or else there will be a new line
                               #Needs sys.stdout.write to remove any white space inbetween the characters
    numSpace = numSpace - 1
    numHash = numHash + 1
    print ""
    

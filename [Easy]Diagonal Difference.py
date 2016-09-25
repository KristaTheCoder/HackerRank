#!/bin/python

import sys

n = int(raw_input().strip()) #rows of matrix
a = []
for a_i in xrange(n): #generates lists
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
i = 0
sum1 = 0
sum2 = 0
j = len(a_temp) - 1
while(i < len(a_temp)):
    sum1 += a[i][i]
    sum2 += a[i][j]
    i = i+ 1
    j = j-1
answer  = abs(sum1 - sum2)
print answer

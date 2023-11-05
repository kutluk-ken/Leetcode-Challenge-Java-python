#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    swap = 0
    while q != sorted(q):
        for i in range(len(q)-1):
            if q[i] - i > 3:
                print('Too chaotic')
                return
            # Bubble sort!
            if q[i] > q[i+1]:
                swap+=1
                q[i], q[i+1] = q[i+1], q[i]

    print(swap)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

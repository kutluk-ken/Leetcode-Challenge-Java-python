#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    for i in range(len(petrolpumps)):
        if petrolpumps[i][0] < petrolpumps[i][1]:
            continue
        else:
            j = 0
            fuel = 0
            cost = 0
            while j < len(petrolpumps):
                if i+j > len(petrolpumps)-1:
                    k = i + j - len(petrolpumps)
                    fuel += petrolpumps[k][0]
                    cost += petrolpumps[k][1]
                    if fuel < cost:
                        break
                    else:
                        j+=1
                else:
                    fuel += petrolpumps[i+j][0]
                    cost += petrolpumps[i+j][1]
                    if fuel < cost:
                        break
                    else:
                        j+=1
            if j == len(petrolpumps):
                return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

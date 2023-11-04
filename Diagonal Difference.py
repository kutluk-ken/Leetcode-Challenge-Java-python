#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # dia_1 = 0
    # for i in range(len(arr[0])):
    #     dia_1+=arr[i][i]
    # dia_2 = 0
    # i = 0
    # j = len(arr[0])-1
    # while i != len(arr[0]):
    #     dia_2 += arr[i][j]
    #     i+=1
    #     j-=1
    # return abs(dia_1 - dia_2)

     # Better solution
    
    left_dia, right_dia = 0, 0
    n = len(arr[0])
    for i in range(n):
        left_dia += arr[i][i]
        right_dia += arr[i][n-i-1]
        
    return abs(left_dia - right_dia)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

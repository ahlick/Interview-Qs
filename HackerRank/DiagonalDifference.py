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
    RightDiagonal = 0
    LeftDiagonal = 0
    yRightCoordinate = n-1
    yLeftCoordinate = 0
    for i in range (0, n):
        RightDiagonal = RightDiagonal + arr[i][yRightCoordinate]
        LeftDiagonal = LeftDiagonal + arr[i][yLeftCoordinate]
        yRightCoordinate -= 1
        yLeftCoordinate += 1
    TotalDifferece = abs(RightDiagonal - LeftDiagonal)
    return TotalDifferece
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

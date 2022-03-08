#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positiveNum = 0
    negativeNum = 0
    zeroNum = 0
    for i in range (0, n):
        if arr[i] > 0:
            positiveNum += 1
        elif arr[i] < 0:
            negativeNum += 1
        elif arr[i] == 0:
            zeroNum += 1
    posProp = positiveNum/n
    negProp = negativeNum/n
    zeroProp = zeroNum/n
    print (posProp)
    print (negProp) 
    print (zeroProp) 
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

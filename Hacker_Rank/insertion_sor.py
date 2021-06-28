# Toy example. Just bring the last element to its spot.
# don't swap. print every line.
# https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    stored_val = arr[n-1]
    for i in reversed(range(n-1)):
        if arr[i] > stored_val and i!=0:
            arr[i+1] = arr[i]
            print(*arr, sep=' ')
        elif i==0 and arr[i] > stored_val:
            arr[i+1] = arr[i]
            print(' '.join([str(x) for x in arr]))
            arr[i] = stored_val
            print(' '.join([str(x) for x in arr]))
        else:
            arr[i+1] = stored_val
            print(*arr, sep=' ')
            break
        
def insertionSort2(n, arr):
    for i in range(n):
        for j in reversed(range(i)):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        if i != 0:
            print(*arr, sep=' ')
        
        

if __name__ == '__main__':
    arr = '2 3 4 5 6 7 8 9 10 1'.split(' ')
    arr = [int(x) for x in arr]
    n=len(arr)
    # insertionSort1(n, arr)
    arr2 = [int(x) for x in '1 4 3 5 6 2'.split(' ')]
    n2=len(arr2)
    insertionSort2(n2, arr2)

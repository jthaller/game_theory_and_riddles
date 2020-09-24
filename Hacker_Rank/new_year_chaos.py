#New Year Chaos
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=arrays

#!/bin/python3

# sample input 
# 2  ## number of test cases
# 5  ## number of people in queue
# 2 1 5 3 4  ## order of people in cue after the bribes
# 5
# 2 5 1 3 4

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2: #if last position 2 larger than its initial spot
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i): #check if swapped. max is so you don't get negative index
            if q[j] > q[i]:
                bribes+=1
    print(bribes)
    
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

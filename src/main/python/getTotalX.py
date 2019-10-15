#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    no_of_int=0
    max_range_a=max(a)
    min_range_b=min(b)

    for i in range(max_range_a, min_range_b+1):
        is_factor_of_a=True
        is_factor_of_b=True
        for j in range(len(a)):
            if i % a[j] > 0:
                is_factor_of_a=False
                break
        if is_factor_of_a:
            for m in range(len(b)):
                if b[m] % i > 0:
                    is_factor_of_b=False
                    break

        if is_factor_of_a and is_factor_of_b:
            no_of_int+=1
    #print(no_of_int)
    return no_of_int


if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='C:\\workspace\\python\\OS_Environ\\getTotalX.txt'
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input=input().rstrip().split()

    n=int(first_multiple_input[0])

    m=int(first_multiple_input[1])

    arr=list(map(int, input().rstrip().split()))

    brr=list(map(int, input().rstrip().split()))

    total=getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

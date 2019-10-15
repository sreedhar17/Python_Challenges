#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    first=x1 + v1
    second=x2 + v2
    result="NO"
    if x1 > x2:
        dividend=x1 - x2
    else:
        dividend=x2 - x1

    if v1 > v2:
        divisor=v1 - v2
    else:
        divisor=v2 - v1

    try:
        print(dividend, divisor)
        if dividend == divisor:
            return "NO"
        else:
            mod=dividend % divisor
    except:
        return "NO"

    print(dividend, divisor, mod)

    if (x2 > x1 and v2 > v1) or (x1 != x2 and v1 == v2) or (x1 == x2 and v1 != v2) or mod > 0:
        result="NO"
    else:
        while True:
            first+=v1
            second+=v2
            if first == second:
                result="YES"
                break
    return result


if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='C:\\workspace\\python\\OS_Environ\\kangaroo.txt'
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2=input().split()

    x1=int(x1V1X2V2[0])

    v1=int(x1V1X2V2[1])

    x2=int(x1V1X2V2[2])

    v2=int(x1V1X2V2[3])

    result=kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

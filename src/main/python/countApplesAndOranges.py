#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    appleCnt=0
    orangeCnt=0

    for i in range(len(apples)):
        if s <= a+apples[i] <= t:
            appleCnt+=1
    for j in range(len(oranges)):
        if s <= b+oranges[j] <= t:
            orangeCnt+=1
    print(appleCnt)
    print(orangeCnt)


if __name__ == '__main__':
    st=input().split()

    s=int(st[0])

    t=int(st[1])

    ab=input().split()

    a=int(ab[0])

    b=int(ab[1])

    mn=input().split()

    m=int(mn[0])

    n=int(mn[1])

    apples=list(map(int, input().rstrip().split()))

    oranges=list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    # Write your code here
    # print(grades)
    res=[]
    for i in range(len(grades)):

        quotient=grades[i] // 5
        mod=grades[i] % 5

        next_multiple_of_5=(quotient + 1) * 5

        if next_multiple_of_5 - grades[i] < 3 and next_multiple_of_5 >= 40:
            res.append(next_multiple_of_5)
        else:
            res.append(grades[i])

    return res


if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='C:\\workspace\\python\\OS_Environ\\test.txt'
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    grades_count=int(input().strip())

    grades=[]

    for _ in range(grades_count):
        grades_item=int(input().strip())
        grades.append(grades_item)

    result=gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    no_of_days_arr=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year=False
    if year >1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 > 0):
            is_leap_year=True
        else:
            is_leap_year=False
    else:
        if year % 4 == 0:
            is_leap_year=True
        else:
            is_leap_year=False

    no_of_days=0
    month=0
    day=0
    for i in range(len(no_of_days_arr)):
        no_of_days+=no_of_days_arr[i]
        month+=1
        if month == 2 and is_leap_year:
            no_of_days+=1

        if no_of_days < 256 and 256 - no_of_days < no_of_days_arr[i + 1]:
            month+=1
            day=256 - no_of_days
            break
        else:
            continue
    dayOfProgrammer=str("{:02d}".format(day)) + "." + str("{:02d}".format(month)) + "." + str(year)
    print(dayOfProgrammer)
    return dayOfProgrammer


if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='C:\\workspace\\python\\OS_Environ\\dayOfProgrammer.txt'
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    year=int(input().strip())

    result=dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

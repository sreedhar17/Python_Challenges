import os


# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    for i in range(len(s)):
        no_of_portions=0
        for j in range(m):
            if i + j < len(s):
                no_of_portions+=s[i + j]
            else:
                break
        if no_of_portions == d:
            count+=1
    return count


if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='C:\\workspace\\python\\OS_Environ\\birthday.txt'
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    n=int(input().strip())

    s=list(map(int, input().rstrip().split()))

    dm=input().rstrip().split()

    d=int(dm[0])

    m=int(dm[1])

    result=birthday(s, d, m)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()

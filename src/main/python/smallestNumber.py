def solution(N):
    result=""
    length=len(str(N))
    print("length:", length)

    if N < 10:
        result=0
        return result

    for i in range(length - 1):
        result+="9"
    print("result:::",result)
    return int(result) + 1
    #pass


if __name__ == '__main__':
    N=127
    x=solution(N)
    print("X::::::", x)
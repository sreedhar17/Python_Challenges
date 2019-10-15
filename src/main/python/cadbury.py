
def TotalCount(M, N, P, Q):
    count=0
    for l in range(M, N + 1):
        for b in range(P, Q + 1):
            count+=CountPerChocolateBar(l, b)
    return count


def CountPerChocolateBar(l, b):
    count=0
    while True:
        longer=max(l, b)
        shorter=min(l, b)
        count+=1
        diff=longer - shorter
        if diff == 0:
            return count
        else:
            l=min(l, b)
            b=diff


if __name__ == "__main__":
    numbers=input("Number: ")
    M,N,P,Q = int(numbers.split()[0]),int(numbers.split()[1]),int(numbers.split()[2]),int(numbers.split()[3])
    tc=TotalCount(M, N, P, Q)
    print(tc)

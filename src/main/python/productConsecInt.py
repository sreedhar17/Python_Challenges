def solution(A,B):
    mod = B%A
    multi_counter = 0
    loopRange = B-A
    if A==B:
        return multi_counter
    for i in range(loopRange):
        X = i+2
        product = X*(X+1)
        mod+=1
        if product>=A and product<=B :
            multi_counter+=1
        elif product>B:
            break
    return multi_counter


if __name__ == '__main__':
    A=6
    B=20
    x = solution(A,B)
    print(x)


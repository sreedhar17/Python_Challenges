def starTriangle(r):
    for x in range(r):
        # print('' * (r - x - 1) + '*')
        str1='' * (r - x - 1) + '*' * (2 * x + 1)
        print(str1.center(17))


if __name__ == "__main__":
    starTriangle(9)

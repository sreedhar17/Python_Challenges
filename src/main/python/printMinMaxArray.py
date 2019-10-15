def get_square_numbers(n=10):
    lst=[i * i for i in range(-3, n)]
    print(lst)
    return lst


def min_and_max(arr):
    return min(arr), max(arr)


def main():
    a=get_square_numbers(6)[1:]
    b=min_and_max(set(a))
    print("{}".format(b))


if __name__ == "__main__":
    main()

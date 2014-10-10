def is_decreasing(seq):
    x = 0
    if len(seq) == 1:
        return True

    while(x < (len(seq)-1)):
        if seq[x] > seq[x+1]:
            return True
        x = x + 1
    return False


def main():
    print(is_decreasing([5, 4, 3, 2, 1]))
    print(is_decreasing([1, 2, 3]))
    print(is_decreasing([100, 50, 20]))
    print(is_decreasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()

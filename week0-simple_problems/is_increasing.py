def is_increasing(seq):
    x = 0
    if len(seq) == 1:
        return True

    while(x < (len(seq)-1)):
        if seq[x] >= seq[x+1]:
            return False
        x = x + 1
    return True


def main():
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))


if __name__ == '__main__':
    main()

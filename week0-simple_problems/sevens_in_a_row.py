def sevens_in_a_row(arr, n):
    count = 0
    for x in arr:
        if x == 7:
            count = count + 1
        else:
            if count == n:
                return True
            count = 0
    return False


def main():
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
    print(sevens_in_a_row([1, 7, 1, 7, 7], 4))
    print(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
    print(sevens_in_a_row([7, 2, 1, 6, 2], 1))


if __name__ == '__main__':
    main()

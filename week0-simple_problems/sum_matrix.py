def sum_matrix(x):
    total = 0
    for list in x:
        for number in list:
            total += number
    return total


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sum_matrix(m))
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(sum_matrix(m))
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(sum_matrix(m))

if __name__ == '__main__':
    main()

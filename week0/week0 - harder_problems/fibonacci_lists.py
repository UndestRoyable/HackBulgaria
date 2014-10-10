def nth_fib_lists(listA, listB, n):
    position = 2
    while position < n + 1:
        next = listA + listB
        listA = listB
        listB = next
        position += 1

    return listA


def main():
    print(nth_fib_lists([1], [2], 1))
    print(nth_fib_lists([1], [2], 2))
    print(nth_fib_lists([1, 2], [1, 3], 3))
    print(nth_fib_lists([], [1, 2, 3], 4))
    print(nth_fib_lists([], [], 100))


# PROGRAM RUN
if __name__ == "__main__":
    main()

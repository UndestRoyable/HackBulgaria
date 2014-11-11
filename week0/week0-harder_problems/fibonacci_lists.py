def nth_fib_lists(listA, listB, n):
    position = 2
    while position < n + 1:
        next = listA + listB
        listA = listB
        listB = next
        position += 1

    return listA

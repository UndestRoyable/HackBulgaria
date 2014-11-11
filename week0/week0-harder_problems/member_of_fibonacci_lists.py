def member_of_nth_fib_lists(listA, listB, needle):
    position = 2
    while position < len(needle) + 1:
        next = listA + listB
        listA = listB
        listB = next
        position += 1

        if listB == needle:
            return True

    return False


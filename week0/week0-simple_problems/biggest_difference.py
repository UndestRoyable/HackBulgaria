def biggest_difference(arr):
    arr.sort()
    last_element = len(arr)-1
    difference = arr[0] - arr[last_element]
    return difference


def main():
    print(biggest_difference([1, 2]))
    print(biggest_difference([1, 2, 3, 4, 5]))
    print(biggest_difference([-10, -9, -1]))
    #print(biggest_difference(range(100)))
    #'range' object has no attribute 'sort'.....

if __name__ == '__main__':
    main()

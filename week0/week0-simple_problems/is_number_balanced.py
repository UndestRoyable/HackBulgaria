def is_number_balanced(n):
    number = number_to_list(n)
    lenth = len(number)
    #print(number)
    #left=0
    #print(number[left])

    left = 0
    sum_left = 0

    if lenth % 2 == 0:
        while (left < lenth//2):
            sum_left = sum_left + number[left]
            left = left + 1
    else:
        while (left <= lenth//2):
            sum_left = sum_left + number[left]
            left = left + 1

    right = lenth // 2
    sum_right = 0

    while (right <= lenth-1):
        sum_right = sum_right + number[right]
        right = right + 1

    if sum_right == sum_left:
        return True
    return False


def number_to_list(n):
    list = []
    my_number = n
    while (my_number > 0):
        my_digit = my_number % 10
        list = [my_digit] + list
        my_number = my_number // 10
        #print(n)
    return list


def main():
    print('is_number_balanced(9)')
    print(is_number_balanced(9))
    print('is_number_balanced(11)')
    print(is_number_balanced(11))
    print('is_number_balanced(13)')
    print(is_number_balanced(13))
    print('is_number_balanced(121)')
    print(is_number_balanced(121))
    print('is_number_balanced(4518)')
    print(is_number_balanced(4518))
    print('is_number_balanced(28471)')
    print(is_number_balanced(28471))
    print('is_number_balanced(1238033)')
    print(is_number_balanced(1238033))

if __name__ == '__main__':
    main()

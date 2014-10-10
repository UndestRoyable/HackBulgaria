def is_int_palindrome(n):
    if number_to_list(n) == number_to_listTwo(n):
        return True
    return False


def number_to_list(n):
    list = []
    my_number = n
    while my_number > 0:
        my_digit = my_number % 10
        list = [my_digit] + list
        my_number = my_number // 10
        #print(n)
    return list


def number_to_listTwo(n):
    list = []
    my_number = n
    while my_number > 0:
        my_digit = my_number % 10
        list = list + [my_digit]
        my_number = my_number // 10
        #print(n)
    return list


def main():
    print(is_int_palindrome(1))
    print(is_int_palindrome(42))
    print(is_int_palindrome(100001))
    print(is_int_palindrome(999))
    print(is_int_palindrome(123))


if __name__ == '__main__':
    main()

def number_to_list(n):
    list_of_numbers = []
    number = n

    while number > 0:
        digit = number % 10
        list_of_numbers = [digit] + list_of_numbers
        number = number // 10
    return list_of_numbers


def main():
    print(number_to_list(123))
    print(number_to_list(99999))
    print(number_to_list(123023))

if __name__ == '__main__':
    main()

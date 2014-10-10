def nth_fibonacci(number):
    if number <= 2:
        return 1

    else:
        return nth_fibonacci(number - 1) + nth_fibonacci(number - 2)


def main():

    print (nth_fibonacci(1))

    print (nth_fibonacci(2))

    print (nth_fibonacci(3))

    print (nth_fibonacci(10))

if __name__ == "__main__":
    main()

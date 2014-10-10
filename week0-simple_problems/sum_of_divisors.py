def sum_of_divisors(n):
    sum = 0
    i = n
    while i > 0:
        if n % i == 0:
            sum += i
        i = i - 1
    return sum


def main():
    print(sum_of_divisors(8))
    print(sum_of_divisors(7))
    print(sum_of_divisors(1))
    print(sum_of_divisors(1000))

if __name__ == '__main__':
    main()

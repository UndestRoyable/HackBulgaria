def is_prime(n):
    i = n
    div_sum = 0
    if n == 1:
        return False
    while i > 0:
        if n % i == 0:
            div_sum += i
        i = i - 1
    if div_sum > 1 + n:
        return False
    return True


def main():
    print (is_prime(1))
    print (is_prime(2))
    print (is_prime(8))
    print (is_prime(11))
    print (is_prime(-10))

if __name__ == "__main__":
    main()

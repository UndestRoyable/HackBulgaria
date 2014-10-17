def is_prime(number):
    if number <= 1:
        return False

    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False
        else:
            divisor += 1

    return True


def goldbach(n):
    goldbach = []

    for number in range(n):
        if is_prime(number):
            if is_prime(n - number):
                goldbach.append((number, n - number))

    for current in goldbach:
        for next in goldbach:
            if current[0] == next[0]:
                if goldbach.index(current) != goldbach.index(next):
                    del goldbach[goldbach.index(next)]
    return goldbach



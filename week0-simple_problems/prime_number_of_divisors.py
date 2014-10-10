from is_prime import is_prime
from sum_of_divisors import sum_of_divisors


def prime_number_of_divisors(n):
    divs_sum = sum_of_divisors(n)
    prime = is_prime(divs_sum)

    return prime


def main():
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))

if __name__ == "__main__":
    main()

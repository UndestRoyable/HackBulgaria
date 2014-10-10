def simplify_fraction(nominator_denominator):
    nominator = nominator_denominator[0]
    denominator = nominator_denominator[1]
    for i in range(1, nominator + 1):
        if nominator % i == 0 and denominator % i == 0:
            nominator //= i
            denominator //= i
    return (nominator, denominator)


def main():

    print(simplify_fraction((3, 9)))
    print(simplify_fraction((1, 7)))
    print(simplify_fraction((4, 10)))
    print(simplify_fraction((63, 462)))

if __name__ == "__main__":
    main()

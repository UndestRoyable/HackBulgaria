def sort_fractions(fractions):
    result = []
    calculated = []

    for fraction in fractions:
        value = fraction[0] / fraction[1]
        calculated.append([value, fraction])

    calculated.sort()

    for fraction in calculated:
        result.append(fraction[1])

    return result


def main():

    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))  
if __name__ == "__main__":
    main()

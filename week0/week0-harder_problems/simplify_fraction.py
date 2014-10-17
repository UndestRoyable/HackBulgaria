def simplify_fraction(nominator_denominator):
    nominator = nominator_denominator[0]
    denominator = nominator_denominator[1]
    for i in range(1, nominator + 1):
        if nominator % i == 0 and denominator % i == 0:
            nominator //= i
            denominator //= i
    return (nominator, denominator)


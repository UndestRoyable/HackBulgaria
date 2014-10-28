def greatest_common_divisor(a,b):
    if a == b:
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    return greatest_common_divisor(a, b - a)
def simplify_fraction(fraction):
    gcd = greatest_common_divisor(fraction[0],fraction[1])
    return (fraction[0] // gcd, fraction[1] // gcd)


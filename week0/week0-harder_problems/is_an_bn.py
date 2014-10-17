def is_an_bn(string):
    middle = len(string) // 2
    first_half = string[:middle]
    second_half = string[middle:]

    if len(string) == 1 or string == "":
        return True

    if first_half[0] == "a" and not "b" in first_half:
        if second_half[0] == "b" and not "a" in second_half:
            if first_half.count("a") == second_half.count("b"):
                return True

    return False


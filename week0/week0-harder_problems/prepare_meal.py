def prepare_meal(number):
    output = []
    while number % 3 == 0:
        output.append("spam")
        number //= 3
    if number % 5 == 0:
        if output:
            output.append("and")
        output.append("eggs")
    return " ".join(output)
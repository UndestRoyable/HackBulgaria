def iterations_of_nan_expand(expand):
    not_a = "Not a "
    answer = expand.count(not_a)
    return answer


def main():
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN"))
    print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    print(iterations_of_nan_expand("Show these people!"))

if __name__ == "__main__":
    main()

def nan_expand(times):
    not_a_nan = "Not a NaN"
    not_a = "Not a "
    empty_string = ""
    if times == 0:
        return empty_string
    elif times == 1:
        return not_a_nan
    else:
        return (not_a*times) + not_a_nan


def main():
    print (nan_expand(0))
    print (nan_expand(1))
    print (nan_expand(2))
    print (nan_expand(3))

if __name__ == "__main__":
    main()

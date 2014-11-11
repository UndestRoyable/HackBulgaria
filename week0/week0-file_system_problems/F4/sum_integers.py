
from sys import argv


def sum_integers_from_file(filename):

    content = open(filename, "r")

    integers_Sum = 0
    for line in content:
        integers = line.split()
        for integer in integers:
            integers_Sum += int(integer)
    content.close()
    return integers_Sum


def main():

    filename = argv[1]
    print(sum_integers_from_file(filename))


if __name__ == '__main__':
    main()

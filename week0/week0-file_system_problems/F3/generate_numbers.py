import sys
from random import randint


def main():

    file_to_write = sys.argv[1]
    randInt_count = 0
    randInt_count = int(sys.argv[2])

    file = open(file_to_write, "w")
    for i in range(randInt_count):
        rand_number = randint(0, 1001)
        file.write(str(rand_number))
        file.write("\n")
    file.close()

if __name__ == '__main__':
    main()

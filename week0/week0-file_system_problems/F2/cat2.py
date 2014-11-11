# cat.py
import sys


def main():
    first_to_read = sys.argv[1]
    second_to_read = sys.argv[2]
    open_file_1 = open(first_to_read, "r")
    open_file_2 = open(second_to_read, "r")

    first_file_content = open_file_1.read()
    second_file_content = open_file_2.read()

    print(first_file_content)
    print(second_file_content)

    file.close()

if __name__ == '__main__':
    main()

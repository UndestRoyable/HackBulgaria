import sys


def main():
    first_to_read = sys.argv[1]
    second_to_read = sys.argv[2]
    open_file_1 = open(first_to_read, "r")
    open_file_2 = open(second_to_read, "r")
    file_to_write_on = "MEGATRON.txt"
    write_file_opened = open(file_to_write_on, "w")

    file1_content = open_file_1.read()
    file2_content = open_file_2.read()

    write_file_opened.write(file1_content)
    write_file_opened.write(file2_content)

    open_file_2.close()
    open_file_1.close
    write_file_opened.close()


if __name__ == '__main__':
    main()

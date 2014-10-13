import sys


def count_lines(filename):
    
    opened_file = open(filename, "r")

    contents = opened_file.read()
    lines_count = contents.count("\n") + 1 #counts the endline symbols and +1 for the 1st line
    opened_file.close()
    return lines_count


def count_chars(filename):
    chars_count = 0
    opened_file = open(filename, "r")
    for line in opened_file:
        chars_count += len(line)
    opened_file.close()
    return chars_count


def count_words(filename):
    words = []

    opened_file = open(filename, "r")

    for line in opened_file:
        line = line.split()
        for word in line:
            words.append(word)
    opened_file.close()
    return len(words)



def main():

    filename = sys.argv[2]
    if sys.argv[1] == "chars":
        print(count_chars(filename))

    elif sys.argv[1] == "words":
        print(count_words(filename))

    elif sys.argv[1] == "lines":
        print(count_lines(filename))

    else:
        print("Invalid command")


if __name__ == '__main__':
    main()

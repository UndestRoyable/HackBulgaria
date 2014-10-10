from random import randint
import sys


def main():
    file_name = sys.argv[1]
    randInt_count = int(sys.argv[2])
    content = []
    for i in range(randInt_count):
        content.append(randint(1,1000))

    open_file = open(file_name,"w")
    open_file.write(str(content))
    file_content = open_file.read()
    print(file_content)

    file.close()

# FIX

if __name__ == '__main__':
    main()


    
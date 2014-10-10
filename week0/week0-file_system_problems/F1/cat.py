# cat.py
import sys


def main():
    file_to_read = sys.argv[1]
    open_file = open(file_to_read,"r")
    content = open_file.read()
    print (content)
    
    file.close()
if __name__ == '__main__':
    main()
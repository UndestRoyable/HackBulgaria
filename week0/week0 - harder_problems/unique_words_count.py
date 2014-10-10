
def unique_words_count(words):
    return len(set(words))


def main():

    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))

if __name__ == "__main__":
    main()

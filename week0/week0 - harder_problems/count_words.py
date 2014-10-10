def count_words(words):
    a = {}
    words_set = set(words)
    for word in words_set:
        word_counter = 0
        for i in words:
            if word == i:
                word_counter += 1
                a[word] = word_counter
    return a


def main():

    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))

if __name__ == "__main__":
    main()

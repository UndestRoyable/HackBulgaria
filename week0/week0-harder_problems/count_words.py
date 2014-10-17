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

